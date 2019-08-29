+++
title = "Research"
date = "2014-04-09"
description = "Research"
keywords = ["Research"]
+++

> ## Mission

Goal of the medical image analysis laboratory is researches on medical image analysis based on the state of the art technologies of pattern recognition, machine learning, artificial intelligence and big data analysis, and development of computer aided-diagnosis systems using the research results.

> ## Background

Advances in image capture devices have made it possible to image the inside of the human body in 3D with a resolution of 1mm or less. As a result, it became possible to detect extremely early cancers. However, examining the image with only the naked eye from hundreds or more than 1,000 is a great burden on doctors. Therefore, the development of an image processing program that supports doctors by automatically analyzing images using computers and recognizing abnormalities in organs and their interiors is required. Recently, a new academic field called computational anatomy has been born that mathematically and statistically describes changes in the shape and concentration of organs in the human body. The results in this field have been confirmed to show better performance than before, as it is used in processing that automatically recognizes organs and diseases from images. In the following, after showing the results of research related to computational anatomy, we will introduce examples of research on image processing such as organ recognition and tumor recognition using the results. Recently, attention has been focused on image analysis not only for the fetus and the living body but also for the human body after death, and we are working on this, but we will also introduce examples of these studies.
<!-- ![slide1](/img/research/slide1_E.png) -->
<div align="center"><img src="/img/research/slide1_E.png"  width=50% title="slide1"></div>

> ## Research

### 1. Fundamental technologies

#### 1-1 Computational anatomy
We have studied on statistical shape models (SSMs) of human trunk that describe statistical shape variation of organs. Following figure shows an example of SSMs of several organs in a human trunk, in which not only statistical shape variations of individual organs but also statistical correlations between neighboring organs were modeled.
<!-- ![slide2](/img/research/slide2_E.jpg "Saito et al. 2013") -->
<div align="center"><img src="/img/research/slide2_E.jpg"  width=50% title="slide2"></div>

We are now extending such statistiacl model so as to describe statistical variation along time axis, resolution axis, functional axis and pathological axis in [multi-disciplinary computational anatomy project](http://wiki.tagen-compana.org/mediawiki/index.php/Main_Page)．

### 2. Applications

#### 2-1 Automated organ recognition
##### １）Single organ recognition (lung, liver, pancreas...)
Segmentation problem of organ with average shapes and without pathology has been solved. We focus on segmentation problem of organ with atypical shape and/or pathological lesion.

Segmentation with SSM is effective approach to prevent unnatural shape in segmentation of organ with pathological lesion. This figure shows graph cuts with multiple shapes, in which it successfully recognizes lung area with pathological lesion.

<!-- ![slide3](/img/research/slide3_E.jpg "Nakagomi et al., 2013") -->
<div align="center"><img src="/img/research/slide3_E.jpg"  width=50% title="slide3"></div>

We proposed a sparse modeling based approach with lesion basis for segmentation of an organ with an atypical shape and large pathological lesions.
<!-- ![slide4](/img/research/slide4_E.jpg "Umetsu et al., 2014") -->
<div align="center"><img src="/img/research/slide4_E.jpg"  width=50% title="slide4"></div>

A relaxed conditional SSM was presented to manage errors in conditions that involve an irregular shape of an organ and/or lesions. A sequentially graph cuts based segmentation algorithm with the relaxed conditional SSM was presented to show the effectiveness of such an SSM in segmentation.
<!-- ![slide5](/img/research/slide5_E.jpg "Tomoshige et al., 2014") -->
<div align="center"><img src="/img/research/slide5_E.jpg"  width=50% title="slide5"></div>

##### ２）Multi-organ segmentation
We proposed atlas guided expectation and maximization (EM) algorithm for statistical parameter estimation and maximum a posteriori (MAP) segmentation followed by multiple level sets in which overlap between neighboring level sets are minimized.
<!-- ![slide6](/img/research/slide6_E.jpg "Shimizu et al., 2007") -->
<div align="center"><img src="/img/research/slide6_E.jpg"  width=50% title="slide6"></div>

#### 2-2 Automated recognition of pathological lesions
##### １）Liver tumors in CT volume
We proposed an ensemble learning based liver tumor segmentation algorithm which was proved to be the best in the competition in conjunction with MICCAI2008.
<!-- ![slide7](/img/research/slide7_E.jpg "Narihira et al., 2013") -->
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
<!-- ![slide8](/img/research/slide8_E.jpg) -->
<div align="center"><img src="/img/research/slide8_E.jpg"  width=50% title="slide8"></div>

##### ２）Postmortem computational anatomy and organ recognition with large deformation
We have studied on postmortem computational anatomy in which postmortem organ’s shape variation can be modeled by a postmortem SSM. Following slide shows average shapes of in-vivo and postmortem livers, where right lobe of the postmortem liver goes up due to respiratory arrest and left lobe goes down due to dilation of heart. We also developed a segmentation algorithm based on the postmortem SSM.
<!-- ![slide9](/img/research/slide9_E.jpg "Saito et al., 2013") -->
<div align="center"><img src="/img/research/slide9_E.jpg"  width=50% title="slide9"></div>

In addition, we are developing a temporal model of a postmortem CT volume by collaborating with Tokai Univ. and Hamburg Univ.

##### ３）Cause of death and postmortem time
Once postmortem organs are recognized, machine learning based algorithm estimates cause of death and postmortem time. This work is collaboration work with Yamaguchi Univ. and Fukui Univ.
