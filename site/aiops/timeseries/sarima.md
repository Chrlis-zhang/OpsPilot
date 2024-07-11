# SARIMA
## 算法简介

SARIMA（季节性自回归整合滑动平均）是一种用于时序预测的统计模型，它扩展了ARIMA（自回归整合滑动平均）模型。一般时序数据很难满足平稳性要求，比较常用的转化方法就是差分，所以<font color=red>ARIMA(p,q,d)</font>在<font color=red>ARMA(p,q)</font>的基础上将差分的过程包含了进来，因此ARIMA可以处理非平稳时间序列，但是不能很好处理周期性序列。因此<font color=red>SARIMA(p,q,d,P,Q,D,s)</font>又在<font color=red>ARIMA(p,q,d)</font>的基础上进行拓展增加了P Q D三个超参以及一个季节性周期参数s，可以支持带有季节性成分的时序数据。
## 使用场景
SARIMA适用于具有<font color=red>季节性变化</font>的时间序列数据，且<font color=red>数据量要较大</font>，数据量太少模型的效果较差。

## 算法原理
SARIMA包括季节性相关项(S)、自回归(AR)、差分(I)和平均移动(MA)四个部分：

(1) **AR（自回归）部分**表示当前值与过去值之间的依赖关系，即当前值与过去若干个时间点的值之间存在线性关系，可以通过PACF确定合适的滞后阶数，对应参数p；

(2) **I（差分）部分**是为了消除数据的非平稳性，通过对时序数据进行差分处理，可以将非平稳时序数据转化为平稳的时序数据，对应参数d；

(3) **MA（移动平均）部分**表示当前值与过去若干个时间点的观测误差之间的依赖关系，可以通过ACF确定合适的滞后阶数，对应参数q；

(4) **S（季节性项）部分**包括季节性回归(SAR)、季节性差分(SI)、季节性移动平均(SMA)和季节性频率(s)四部分，分别对应参数P、D、Q、s。前三个季节性项与ARIMA模型中的对应项具有相似的作用。

总结起来，SARIMA模型利用自回归、差分和移动平均等技术，以及考虑季节性的相关项，对具有季节性和趋势性的时间序列数据进行预测。