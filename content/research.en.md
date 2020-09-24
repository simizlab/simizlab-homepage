+++
title = "Research"
date = "2014-04-09"
description = "Research"
keywords = ["Research"]
+++

## Mission

Goal of the medical image analysis laboratory is researches on medical image analysis based on the state of the art technologies of pattern recognition, machine learning, artificial intelligence and big data analysis, and development of computer aided-diagnosis systems using the research results.

## Background

Advances in image capture devices have made it possible to image the inside of the human body in 3D with a resolution of 1mm or less. As a result, it became possible to detect extremely early cancers. However, examining the image with only the naked eye from hundreds or more than 1,000 is a great burden on doctors. Therefore, the development of an image processing program that supports doctors by automatically analyzing images using computers and recognizing abnormalities in organs and their interiors is required. We will introduce our research along with its concept as below. 

<!--<div align="center"><img src="/img/research/slide1_E.png"  width=50% title="slide1"></div>-->

## Research

### 1. Bone Scintigram

<img src="/img/research/slide_1.png" width=50% title="slide1" hspace=20 align="left">
The bone scintigram is one of the nuclear medicine examination that we often use in clinical because of effectiveness of diagnosis of systemic bone metastases in neoplastic diseases. In this examination, we obtain two 2-dimension images per each patient which consist of front and back of the body. The bone scintigram, which is able to look around a whole body and detect the lesion with highly sesitivity, plays an inportant role in the bone metastasis diagnosis. And, in the Bone Scan Index(BSI) used as method for evaluation of bone metastasis spread quantetitatively, it is important to detect positive accumulation(bone metastasis) accurately. So far, processing of positive accumulation detection by means of U-Net which is based on deep learning have been proposed, but since it processes an image between front and back independently, there were not integrity between front and back detected result. In this research, we propose how to obtain consistent results in both of output s by processing information about front and back bone scintigram simultaneously using "Btrfly-Net".

<br clear="all">


### 2. Super Resolusion
<img src="/img/research/slide_2.png" width=50% title="slide2" hspace=20 align="left">
Recently, the image diagnosis using varieties of medical images such as CT and MR has been carried out, and it plays an significant role in medical diagnosis and treatment. In the image diagnosis, a doctor checks whether normal or abnormal in your body from CT or MR images, and makes decision to subsecuent treatment direction. But, although we demand that images will be high resolution in order to diagnose symptom accurately, due to limitation of shooting conditions(exposure dose and shooting time), the image resolution is often restricted. Therefore, the super-resolution technology, which converts a low resolution(LR) image into high resolution(HR) one, is paid a greatly attension. By restoring a HR image from a LR image, we are expected to detect a disease earlier and grasp a correct posision of a lesion. In this research, we are going to focus on the super-resolution technology, and we achieved restoring high-definition HR images by using Generative Adversarial Networks(GANs) in comparison to conventional methods.

<br clear="all">

### 3. Statistical Model
A statistical model is represented an organ's shape or intensity distribution by several parameters, and used as crucial pre-information in the medical image processing. For example, in the organ segmentation, the statistical model could be constrain conditions for the organ shape and get rid of obviously different shapes from what we would like to aim at, and we are expected to improve segmentation performance.

<br>

#### 3.1. Statistical Shape Model for Human Embryos

---

<img src="/img/research/slide_3.png" width=50% title="slide3" hspace=20 align="left">
In the human growth process, the term that is between 3 and 9 weeks of pregnancy is called the embryo stage, which is important period for shaping organs, and has a risk that  various kinds of abnomals will be happend. In addition, it is said that the 25% of death causes among newborns is a congenital anormaly, thus, the prenatal diagnosis is considerably significant. Therefore, we demand to develop the computed aided diagnosis(CAD) system for growth prediction of a human embryo or the prenatal image diagnosis. However, since organs in the embryo stage change its shape dinamically as it is growing, the conventional statistical shape model(SSM) could not deal with dinamic change of the anatomic structure form depending on time. In this research, we will construct the time and space SSM applying for time change and study in how to make use of the CAD system against prenatal congenital anormaly shapes.

<br clear="all">

<br>


#### 3.2. Statistical Intensity Model for Blood Vessels

---

<img src="/img/research/slide_4.png" width=50% title="slide4" hspace=20 align="left">
A disease caused by abnormal blood flow directly links to death and many cases should be considerably serious.For instance, there are myocardial infarction or angina, which results from humps in the blood vessel due to stagnating blood flow in the blood vessel by arteriosclerosis. Thus, an early detection of anormaly in the blood vessel is essential. A blood vessel segmentation plays an important role in an anormaly detection and it is expected to improve accuracy by applying for the statistical model.In contrast, a model construction forcusing on the dendritic structure such as blood vessels which has complicated its intensity distribution is difficult to make model so little investigation have been proposed so far.In this research, we will target on dendritic structure such as lung blood vessels and bronchus, and study in construction of the statistical intensity model by VAE which is kind of deep generative learning.

<br clear="all">

<br>


### 4. Dementia Aided Diagnosis
<img src="/img/research/slide_5.png" width=50% title="slide5" hspace=20 align="left">
Thanks to the medical technology progress in recent days, our life has been become much more affluent, while aging society is one of the biggest problems in the developed country. One of the issue in aging society is the dementia among elderly people. Unlike forgetfullness due to aging, the dementia is generally recognized as the symptom or state caused by nerve tissue's breaking because of someting disease. The dementia is classified into several types by causes, that is, Alzheimer’s disease(AD)(most case), vascular dementia(VD), frontotemporal dementia (FTD) and dementia with Lewy bodies (DLB) are called 4 major causes. In 3 major causes except VD, there are a lot of cases that we can detect early by means of SPECT examination. Although we can view the state of brain blood flow as an image at SPECT examination, it is difficult for a docter to identify a part of blood flow decline from images and diagnose whether dementia or not. It is also time consuming. Therefore, the computer aided diagnosis system has been demanded. In this research, we are going to develop system that recognize dementia from the SPECT image based on deep learning. 

<br clear="all">



### 5. Organ Segmentation
<img src="/img/research/slide_6.png" width=50% title="slide6" hspace=20 align="left">
An infant image has large variations in organ's density, shape, location and size depending on an individual or its age and due to a low-dose imaging, it would be a low resolution and low SN (signal-to-noise) ratio image.Dealing with these problems, we need the original image  diagnosis aided system instead of what is targeted on adults. Many  segmentation methods based on deep learning have been proposied so far and high accuracy outcomes have been reported, while there is an issue that there are predicted results of unnatural shapes.In this research, we are going to aim at improving liver segmentation performance for infant CT images by applaying the time-space statistical shape model for "3D-Unet" adapted to 3 dimention CT images.

<br clear="all">

### 6. Skin Disease Image Classification
<img src="/img/research/slide_7.png" width=50% title="slide6" hspace=20 align="left">
Skin is tissue covering body surface and the biggest organ in a human body, which is shared about 16% in adult weight. Skin directly contacts out of the body and has a plenty of essential fanctions in order that the human survives such as maintaining moisture, adjusting body temperature, protecting from stimulation and playing a role as the sensory organ. However, skin located in body surface is also the organ that keeps on exposing a lot of outer stimulations such as moisture evapolation, invation of foreign matters and ultraviolet irradiation. These stimulations has possiblity to develop various kinds of disease. A skin cancer, in particular, compared to a cancer developed in other organ, is slow progress and easy to process by early detection and treatment, and makes it possible to reduce burden on patients and doctors. Therefore, we demand to conduct prompt doctor's diagnosis and treatment against skin foreign matters. In this research, we are going to propose methods to improve identification performance using several images targeted on experimental samples consisting of valious kinds of images such as shooting device, angle, scale and background.


<br clear="all">
<br>

<!--
### 1. Fundamental technologies

#### 1-1 Computational anatomy
We have studied on statistical shape models (SSMs) of human trunk that describe statistical shape variation of organs. Following figure shows an example of SSMs of several organs in a human trunk, in which not only statistical shape variations of individual organs but also statistical correlations between neighboring organs were modeled.

<div align="center"><img src="/img/research/slide2_E.jpg"  width=50% title="slide2"></div>

We are now extending such statistiacl model so as to describe statistical variation along time axis, resolution axis, functional axis and pathological axis in [multi-disciplinary computational anatomy project](http://wiki.tagen-compana.org/mediawiki/index.php/Main_Page)．

### 2. Applications

#### 2-1 Automated organ recognition
##### １）Single organ recognition (lung, liver, pancreas...)
Segmentation problem of organ with average shapes and without pathology has been solved. We focus on segmentation problem of organ with atypical shape and/or pathological lesion.

Segmentation with SSM is effective approach to prevent unnatural shape in segmentation of organ with pathological lesion. This figure shows graph cuts with multiple shapes, in which it successfully recognizes lung area with pathological lesion.


<div align="center"><img src="/img/research/slide3_E.jpg"  width=50% title="slide3"></div>

We proposed a sparse modeling based approach with lesion basis for segmentation of an organ with an atypical shape and large pathological lesions.

<div align="center"><img src="/img/research/slide4_E.jpg"  width=50% title="slide4"></div>

A relaxed conditional SSM was presented to manage errors in conditions that involve an irregular shape of an organ and/or lesions. A sequentially graph cuts based segmentation algorithm with the relaxed conditional SSM was presented to show the effectiveness of such an SSM in segmentation.

<div align="center"><img src="/img/research/slide5_E.jpg"  width=50% title="slide5"></div>

##### ２）Multi-organ segmentation
We proposed atlas guided expectation and maximization (EM) algorithm for statistical parameter estimation and maximum a posteriori (MAP) segmentation followed by multiple level sets in which overlap between neighboring level sets are minimized.

<div align="center"><img src="/img/research/slide6_E.jpg"  width=50% title="slide6"></div>

#### 2-2 Automated recognition of pathological lesions
##### １）Liver tumors in CT volume
We proposed an ensemble learning based liver tumor segmentation algorithm which was proved to be the best in the competition in conjunction with MICCAI2008.

<div align="center"><img src="/img/research/slide7_E.jpg"  width=50% title="slide7"></div>

##### ２）Cerebral aneurysm in MR volume
We proposed an algorithm for cerebral aneurysm detection in MR volume. This is a collaborative research with the Univ. of Tokyo.

##### ３）Abnormal accumulation in a bone scintigram
We have studied on automated abnormal accumulation detection in a bone scintigram by collaboration with Osaka city university.

#### 2-3 Embryo analysis
We have studied on embryos of Kyoto Collection so as to model evolution process of Homo sapiens (collaboration with Kyoto Univ.)

#### 2-4 Postmortem analysis
Recently, Autopsy imaging in Japan, Virtopy in Europe have attracted many researchers, in which cause of death are estimated based on postmortem CT and/or MR volumes. We have approached this problem from the viewpoint of medical image analysis.

##### １）Bone fracture
Bone fracture is an important sign to identify cause of death. We proposed an algorithm which combines denoising autoencorder with deep convolutional neural network, to detect bone fractures in a postmortem CT volume.

<div align="center"><img src="/img/research/slide8_E.jpg"  width=50% title="slide8"></div>

##### ２）Postmortem computational anatomy and organ recognition with large deformation
We have studied on postmortem computational anatomy in which postmortem organ’s shape variation can be modeled by a postmortem SSM. Following slide shows average shapes of in-vivo and postmortem livers, where right lobe of the postmortem liver goes up due to respiratory arrest and left lobe goes down due to dilation of heart. We also developed a segmentation algorithm based on the postmortem SSM.

<div align="center"><img src="/img/research/slide9_E.jpg"  width=50% title="slide9"></div>

In addition, we are developing a temporal model of a postmortem CT volume by collaborating with Tokai Univ. and Hamburg Univ.

##### ３）Cause of death and postmortem time
Once postmortem organs are recognized, machine learning based algorithm estimates cause of death and postmortem time. This work is collaboration work with Yamaguchi Univ. and Fukui Univ.
-->