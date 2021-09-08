# 成员交付成果清单

### 0.马驰

- 更新了package的[错误报告](https://gitee.com/mc964203886/OpenEuler-Mainline-RISC-V-Error-Type-August)
- [libreoffice现状调研](https://github.com/plctlab/openEuler-riscv/issues/42)



## 第一批

### 1.孙喆炘 [zhé xīn]

- [BaseOS工程仓及软件包列表](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-obs-baseos-repo.md)
- [BaseOS Project Config & Meta](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-obs-baseos-LFShost.md)
- [ubuntu 上没有 root 权限的用户搭建 QEMU RISC-V 宿主机环境](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/vm-host-no-root-on-ubuntu.md)



bootstrap和baseos的进展现在卡在了[make](https://build.openeuler.org/packages/make/job_history/openEuler:Mainline:RISC-V/standard_riscv64/riscv64)这个包上，但是华为的obs我没权限去操作它的种子文件夹。目前期待PLCT自己的obs环境。



### 2.刘佳伟

- [OSC本地构建](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/OSC本地构建.pdf)，目前遇到一些问题还没成功，如果有成功的同学，欢迎指导。
- [openEuler包构建相关背景知识](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/openEuler包构建相关背景知识.md)



### 3.李诗洋

- [尝试解决i40e包记录](https://gitee.com/lishiyangasdf/open-euler-r-v-learning-notes/blob/master/尝试解决i40e包记录.md)
- [本地构建abrt包和valgrind记录](https://github.com/plctlab/openEuler-riscv/issues/19)



### 4.孙浩翔

- [构建失败]【已解决】 python-jaraco-collections：[链接](https://github.com/plctlab/openEuler-riscv/issues/48)

  相关PR：[链接](https://gitee.com/src-openeuler/python-jaraco-collections/pulls/2)

  OBS相关Request：[链接](https://build.openeuler.org/request/show/346)

- [构建失败]【已解决】python-mistune：[链接](https://gitee.com/openeuler/RISC-V/issues/I48GDD?from=project-issue)

  OBS相关Request：[链接](https://build.openeuler.org/request/show/345)

- 本地构建过程中遇到的问题：[链接](https://github.com/plctlab/openEuler-riscv/issues/107)

- 笔记：[OBS中包的本地构建记录](https://gitee.com/maximsuen/plct-internship-notes/blob/master/6.OBS中包的本地构建记录.md)



## 第二批

### 5.许志凌

- [[构建失败\] gdbus-codegen-glibmm #106](https://github.com/plctlab/openEuler-riscv/issues/106)



### 6.邹通成

- [构建情况汇总](https://github.com/Wenxiang233/PLCT_Documents/blob/main/Obs构建汇总.md)
- [构建方法总结](https://github.com/Wenxiang233/PLCT_Documents/blob/main/构建方法总结.md)



### 7.许嘉玲

- [本地构建libX11包成功](https://github.com/plctlab/openEuler-riscv/issues/20)
- [学习笔记](https://gitee.com/sticky-rice-wine/note/blob/master/学习笔记.docx)
- 尝试本地修改apr包，还未解决



### 8.颛孙宇翔 [zhuān sūn]

双周暂无交付。提交的为9.1之前的内容。个人表示后续会多做贡献。



## 第三批

### 9.高世豪

- [第一周小结](https://github.com/ShiHaoGao/workRecord/blob/main/1stWeek)
- [[excluded练习\]acpid](https://github.com/plctlab/openEuler-riscv/issues/62)
- [[broken练习\]boost](https://github.com/plctlab/openEuler-riscv/issues/60)



### 10.袁政

**实习一周成果：**
PR（一个包）:

- [rear适配riscv64](https://github.com/plctlab/openEuler-riscv/issues/28)

构建失败（两个包、未解决）：

- [arm-trusted-firmware](https://github.com/plctlab/openEuler-riscv/issues/68#event-5258496859)
  gsl：构建失败原因error: Bad exit status from /var/tmp/rpm-tmp.0kkOg2 (%check)，不知道这个报错怎么修改
  unresolvable（三个包、未解决）：
- [log4j](https://github.com/plctlab/openEuler-riscv/issues/59)
  lcr：需要添加子包，具体解决办法正在学习和研究
  rpm-ostree：需要添加子包，具体解决办法正在学习和研究

学会了在线构建但还不太会solve problems，正在studing，



### 11.刘洋

- [第一周小结](https://gitee.com/LiuY328/deliverable/blob/master/README.md#第一周的成果)
- [[broken练习\]efl](https://github.com/plctlab/openEuler-riscv/issues/57)
- [[excluded练习\]bpftrace](https://github.com/plctlab/openEuler-riscv/issues/58)



### 12.温智翔

暂未提交可见交付



### 13.杨心仪

暂未提交可见交付





问题：

1. 现在实习生的问题曝光不够，能力方面看不太出来。

2. 目前就项目而言，卡在一些基础的包上面，gcc、make等等。这些包都不是一般的实习生能够解决的，需要2-3个能力好的同事先解决问题，让事情能够进入正向循环。

   > 目前，项目我觉得卡在关键路径结点了，关键的问题不解决，一般的实习生都很难做出贡献。所以不管怎么push，实习生也难以下手。

3. 还是需要先解决问题，然后再加强培训。

