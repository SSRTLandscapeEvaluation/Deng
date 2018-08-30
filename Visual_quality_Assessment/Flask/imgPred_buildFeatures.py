# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 14:03:14 2018

@author: Ao
"""

import numpy as np
import pandas as pd
import sqlite3
import pickle
import cv2
from sklearn.cluster import KMeans

flatten_lam = lambda lst: [m for n_lst in lst for m in flatten_lam(n_lst)] if type(lst) is list else [
    lst]  # 展平列表的lambda函数

'''定义类，用于处理Start特征检测相关函数'''


class StarFeatureDetector(object):
    def __init__(self):
        self.detector = cv2.xfeatures2d.StarDetector_create()

    def detector(self, img):
        return self.detector.detect(img)  # 对输入图像运行监测器


'''提取王爷图像打分储存到服务器SQLite数据库中的数据'''


def getImgPath():
    connPred = sqlite3.connect('local_data.bd')
    sql = "select * from imageseval"
    data = pd.read_sql(sql=sql, con=connPred)
    print(data[:5])
    return data


'''根据图像打分评价标志'好','中','差'分离数据，提取对应的图像路径'''


def load_training_data(imgPD):
    training_data = []
    #    print(input_folder)
    goodPD = imgPD[imgPD['eval'] == '好']
    mediumPD = imgPD[imgPD['eval'] == '中']
    poorPD = imgPD[imgPD['eval'] == '差']

    training_data.append([{'object_class': 'good', 'image_path': i} for i in goodPD['imagename'].tolist()])
    training_data.append([{'object_class': 'moderate', 'image_path': i} for i in mediumPD['imagename'].tolist()])
    training_data.append([{'object_class': 'poor', 'image_path': i} for i in poorPD['imagename'].tolist()])
    training_dataFlat = flatten_lam(training_data)
    print(training_dataFlat[:5])
    return training_dataFlat[:5]


'''调整图像大小，因已经处理过图像大小，此处定义函数未使用。一般直接使用misc.imresize()方法调整图像大小更为便捷'''


def resize_image(input_img, new_size):
    h, w = input_img.shape[:2]
    scaling_factor = new_size / float(h)
    if w < h:
        scaling_factor = new_size / float(w)
    new_shape = (int(w * scaling_factor), int(h * scaling_factor))
    return cv2.resize(input_img, new_shape)  # 使用cv2.resize()方法调整图像大小


'''提取sift特征'''


def compute_sift_features(img, keypoints):
    if img is None:
        raise TypeError('Invalid input image')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
    keypoints, descriptors = cv2.xfeatures2d.SIFT_create().compute(img_gray, keypoints)
    return keypoints, descriptors


'''定义类处理词袋模型和向量量化'''


class BagOfWords(object):
    def __init__(self, num_clusters=32):
        self.num_dims = 128
        self.num_clusters = num_clusters  # KMeans聚类参数
        self.num_retries = 10

    '''kmeans聚类'''

    def cluster(self, datapoints):
        kmeans = KMeans(self.num_clusters, n_init=max(self.num_retries, 1), max_iter=10, tol=1.0)
        res = kmeans.fit(datapoints)
        centroids = res.cluster_centers_
        return kmeans, centroids

    '''归一化数据'''

    def normalize(self, input_data):
        sum_input = np.sum(input_data)
        if sum_input > 0:
            return input_data / sum_input
        else:
            return input_data

    '''提取SIFT特征'''

    def construct_feature(self, img, kmeans, centroid):
        keypoints = StarFeatureDetector().detect(img)  # 应用处理star特征检测相关函数，返回检测出的特征关键点
        keypoints, feature_vectors = compute_sift_features(img, keypoints)  # 应用SIFT特征提取描述信息
        labels = kmeans.predict(feature_vectors)
        # print(labels)
        feature_vector = np.zeros(self.num_clusters)

        for i, item in enumerate(feature_vectors):
            # print(i,labels[i])
            feature_vector[labels[i]] += 1
        #        print(feature_vector)
        feature_vector_img = np.reshape(feature_vector, ((1, feature_vector.shape[0])))
        return self.normalize(feature_vector_img)


'''图像特征提取'''


class FeatureBuilder(object):
    '''计算图像特征，返回关键点及特征向量'''

    def extract_feature(self, img):
        keypoints = StarFeatureDetector().delect(img)
        # print(len(keypoints),keypoint[:5])
        keypoints, feature_vectors = compute_sift_features(img, keypoints)
        # print(len(keypoints),keypoint[:5])
        # print(len(feature_vectors),[len(i) for i in feature_vecture_vectors[:5]],feature_vectors[0])
        return feature_vectors

    '''提取指定采样图像数量的图像特征，此时图像评价指标有3类“good”“moderate”“poor”'''

    def get_codewords(self, input_map, scaling_size, max_samples=200):
        keypoints_all = []
        count = 0
        cur_class = ''
        for item in input_map:
            if count >= max_samples:
                if cur_class != item['object_class']:
                    count = 0
                else:
                    continue
            count += 1

            if count == max_samples:
                print("Build centroid for", item['object_class'])

            cur_class = item['object_class']
            img = cv2.imread(item['image_path'])

            #            num_dims=128
            feature_vectors = self.extract_feature(img)
            keypoints_all.extend(feature_vectors)
        # print(len(keypoints_all),keypoint_all[0])
        kmeans, centroids = BagOfWords().cluster(keypoints_all)
        # print(kmeans,centroids.shape,centroids)
        return kmeans, centroids


def get_feature_map(input_map, kmeans, centroids, scaling_size):
    feature_map = []
    for item in input_map:
        temp_dict = {}
        temp_dict['object_class'] = item['object_class']
        print("Extracting feature for", item['image_path'])
        img = cv2.imread(item['image_path'])
        #        img=resize_image(img,scaling_ssize)

        temp_dict['feature_vector'] = BagOfWords().construct_feature(img, kmeans, centroids)
        if temp_dict['feature_vector'] is not None:
            feature_map.append(temp_dict)
    print(feature_map[0]['feature_vector'].shape, feature_map[0])
    return feature_map


if __name__ == "__main__":
    resizeImgData = getImgPath()
    training_data = load_training_data(resizeImgData)
    scaling_size = 100
    kmeans, centroids = FeatureBuilder().get_codewords(training_data, scaling_size)

    with open('featK.pkl', 'wb') as f1:
        pickle.dump((kmeans, centroids), f1)
    feature_map = get_feature_map(training_data, kmeans, centroids, scaling_size)
    with open('feature_map.pkl', 'wb') as f2:
        pickle.dump(feature_map, f2)
