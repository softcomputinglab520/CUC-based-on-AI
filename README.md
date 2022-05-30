#introduction

臺灣自古依山傍水，至少從十六世紀開始臺灣人民大部分靠海維生，至今臺灣則是漁業大國，因此自古以來過度捕撈近海，導致近海無魚，而現今臺灣成為遠洋捕撈霸主，原因有三，一、近海無魚，二、科技進步，三、生態保育；臺灣海岸線佔全球海岸線1/400，魚類物種則佔1/10，資源極為豐厚，而本團隊所開發技術，為保育海洋生態枯竭所開發。

該計數技術可利用固定空間與長期時間進行生態分析，例如：本團隊於綠島的石朗潛水區進行CUC進行資料驗證，2022/03進行資料蒐集，又於2022/06進行資料蒐集，相隔3個月，計算相同區域的生物數量是否增減，若遞減其原因有可能梅雨季節的大量雨水導致沿岸地區鹽度下降所致，若遞增則有可能為該生物之捕食者離開該區域等眾多因素，因此本技術(CUC)為關鍵技術之一，還須搭配環境數據(分析鹽度、溶氧、pH值等數據長時間變化)、專家知識(生物、氣象、水質、地質等專業知識)及大數據分析才可完成水下生態分析。



#Demo

https://user-images.githubusercontent.com/106044709/170942766-07eaf8e4-596d-4931-95e8-cc9924fc5abe.mp4


本技術為水下生物計數，該技術為水下生態分析之基礎技術之一

水下生物計數可透過不同的生物訓練資料進行計數，目前版本僅提供龍蝦

本技術所屬國立臺灣海洋大學之人工智慧中心(NTOU-AIRC)與科技部(MOST)

此為水下生物計數與偵測技術開發結果(持續更新中)

目前偵測器使用Faster RCNN(正在驗證 YOLOv5 與 EfficientDET，完成之後將更新至此)

This technology is CUC, which is one of the basic technologies of Marine Ecological Environment analysis.

The CUC can be counted through different creature training data, this version only provides lobster

This work was supported in part by the AI Research Center (AIRC), National Taiwan Ocean University, and in part by the Ministry of Science and Technology of Taiwan (MOST) AI Biomedical Research Center under Grant MOST 110-2634-F-019-002-, and Grant MOST 110-2221-E-019-062-.


This is the result of the development of CUC and Detector technology (continuously updated)

Detector uses Faster RCNN (will update YOLOv5 and EfficientDET)

軟硬體設備：

軟體：

Py3.6 

tensorflow 1.14

CUDA 10.2

cuDNN 7.6

硬體：

i9-9900

RTX2080
