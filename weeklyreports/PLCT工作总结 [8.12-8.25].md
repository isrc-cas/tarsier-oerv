# PLCT工作总结 [8.12-8.25]

## 过去两周的进展

1. 解决包构建失败的问题
   
   - 约10多个包的处理：可在在[issue中搜索[构建失败]查看相关任务](https://gitee.com/openeuler/RISC-V/issues?utf8=%E2%9C%93&issue_search=%5B%E6%9E%84%E5%BB%BA%E5%A4%B1%E8%B4%A5%5D)
   
   - 将excluded:396(其中的60多个包非noarch包添加ExclusiveArch:riscv64后启动构建)、broken:21在obs上进行_service添加启动构建任务：[统计结果](https://github.com/plctlab/openEuler-riscv/blob/main/doc/excluded%2Bbroken.xlsx)
   
     
   
2. D1 oE镜像、文档
   • D1 openEuler 第三版镜像(HDMI接口可用)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-20210817.img.bz2

   • D1上oE镜像(0817版)测试：[在D1上运行8/17日最新的openEuler镜像，配合11.0.10版本的JDK镜像可以成功运行java语言版本的hello world](https://zhuanlan.zhihu.com/p/401285641?utm_source=wechat_session&utm_medium=social&s_r=0)

   

3. 用于加速构建的oE QEMU 镜像-RV64 SMP32版本：https://mirror.iscas.ac.cn/plct/openEuler_SMP32-20210821.tar.bz2  （面向开发者，普通用户可能是不需要的，内含reademe）

   

4. 【进行中】bishengJDK：编译没问题，更改spec后再构建中



## 未来两周计划

4个方面工作：

1. 继续解决构建失败的包，完成21.09发版计划

   - 【本周暂缓】obs构建

   - rpmbuild本地构建

     

2. 9.23演示D1/BishengJDK 图形界面的游戏

   - 【完成】D1+openEuler

   - bishengJDK

   - 桌面图像界面的支持(xfce)

   

3. 运维保障（辅助加速）：构建平台/环境搭建改进

   - 【已完成】构建虚拟机使用PLCT改过的 32c 32g qemu
   - 9.27左右PLCT搭建的OBS将会上线：

   > 约300个 x86 vcore / 400g mem / 32T hdd 和2个 unmatched/8c/16g/1T （D1比x86+QEMU慢所以先不接入了）。
   >
   > 后续PLCTobs如何与华为obs对接：测试OK之后的包，再触发华为的OBS来构建，绕过构建速度慢和大规模失效的问题。

   

4. 以上3项工作涉及的相关测试工作

   

## 问题





## 其它

构建失败分类管理：

欢迎大家一起维护构建失败分类管理：https://gitee.com/openeuler/RISC-V/issues/I45G4I
