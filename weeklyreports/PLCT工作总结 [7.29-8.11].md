# PLCT工作总结 [7.29-8.11]

## 过去两周的进展
1. D1 oE镜像、文档
• D1 openEuler 镜像下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-20210731.img.bz2
• D1 openEuler 第二版镜像(wifi可用)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-enabled-20210810.img.bz2
• D1上oE镜像的构建过程：https://github.com/wxjstz/docs/blob/master/openEuler_D1%E9%95%9C%E5%83%8F%E7%9A%84%E5%88%B6%E4%BD%9C%E8%BF%87%E7%A8%8B.md
2. 解决包构建失败的问题
• 进行中，暂无成功解决的
3. bishengJDK
• 构建rpm包：刚开展

## 未来两周计划
1. 继续跟踪构建失败的包，边学习边尝试解决一些简单的构建失败
2. 完善文档
3. D1+openEuler
4. bishengJDK
5. 桌面图像界面的支持？

## 问题
1. 构建失败的原因是其依赖的包构建失败。——》陷入一种循环中，需要梳理出依赖关系
关注failed的构建失败包