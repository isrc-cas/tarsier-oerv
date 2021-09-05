# openEuler for RISC-V

本项目目的是构建riscv64下的openEuler 操作系统，系统的构建依托于OBS：https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V 。

项目repo：https://gitee.com/openeuler/RISC-V

项目PLCT内部管理repo：https://github.com/plctlab/openEuler-riscv


### 项目总体进展 by 席静

1. 人员招聘与团队建设：建立8实习生团队和基础技能的学习培训
2. [WIP] 继续解决构建失败的包，完成21.09发版计划：计划成功支持3000+包+UI+bishengJDK等特定软件包
   - 约10多个包的处理：可在在[issue中搜索[构建失败]查看相关任务](https://gitee.com/openeuler/RISC-V/issues?utf8=%E2%9C%93&issue_search=%5B%E6%9E%84%E5%BB%BA%E5%A4%B1%E8%B4%A5%5D)
   - 将excluded:396(其中的60多个包非noarch包添加ExclusiveArch:riscv64后启动构建)、broken:21在obs上进行_service添加启动构建任务：[统计结果](https://github.com/plctlab/openEuler-riscv/blob/main/doc/excluded%2Bbroken.xlsx)


3. [WIP]  BaseOS：刚开始，梳理出用于构建riscv linux操作系统的基础包。

   - 第一批构建目标（76个基础包）：https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-obs-baseos-repo.md
   - 构建地址：https://build.openeuler.org/project/show/home:yx971:RISC-V:BaseOS

4. [WIP] 9.23演示D1/BishengJDK 图形界面的游戏

   - [完成] D1+openEuler：D1 openEuler 第三版镜像(HDMI接口可用)下载地址：https://mirror.iscas.ac.cn/plct/openEuler-D1-wifi-hdmi-20210817.img.bz2
   - [WIP] [bishengJDK](https://gitee.com/openeuler/RISC-V/issues/I28H7L?from=project-issue)：编译没问题，更改spec后再次构建中。

5. 桌面图像界面的支持(xfce)：已经基本完成，缺鼠标、键盘等支持。

6. 运维保障（辅助加速）：构建平台/环境搭建改进

   - [完成] 用于加速构建的oE QEMU 镜像-RV64 SMP32版本：https://mirror.iscas.ac.cn/plct/openEuler_SMP32-20210821.tar.bz2  

     > 刚刚实测以gzip为例，在worker02.tarsier上用qemu oE进行osc构建一个包的的速度是build.oE.org的4倍多

   - 共享依赖仓的搭建：https://mirror.iscas.ac.cn/openeuler-sig-riscv/ 

     - 打破循环依赖的包：https://mirror.iscas.ac.cn/openeuler-sig-riscv/forplct/ 
     - 子项目可引入的rpm包：https://mirror.iscas.ac.cn/openeuler-sig-riscv/subprjdep/ 

   - [WIP] PLCT-OBS构建系统：obs worker已经搭建，server正在搭建中。

     - https://build.tarsier-ci.org/   worker01.tarsier-ci.org + worker02.tarsier-ci.org


6. 测试工作

   - D1上oE镜像(0817版)测试：[在D1上运行8/17日最新的openEuler镜像，配合11.0.10版本的JDK镜像可以成功运行java语言版本的hello world](https://zhuanlan.zhihu.com/p/401285641?utm_source=wechat_session&utm_medium=social&s_r=0)
   - 在Qemu RISCV64虚拟机中安装Docker并运行RISCV Linux:https://zhuanlan.zhihu.com/p/399366057 

   

### 实习生和伙伴进展请PR到这里

#### 孙喆炘  [zhé xīn]

PR

- [x265适配riscv64](https://gitee.com/riscv-spare/x265/pulls/1)
- [tbb适配riscv64](https://gitee.com/riscv-spare/tbb/pulls/2)
- [file适配riscv64升级](https://gitee.com/riscv-spare/file/pulls/1)

doc

- [Alpine Linux x86 作为 QEMU RISC-V 宿主机](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/vm-host-AlpineLinux.md)
- [openEuler RISC-V QEMU 环境](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/vm-qemu-openEuler-riscv64.md)
- [在 openEuler 上搭建 osc 本地构建环境](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-osc-build-tools.md)
- [~/.oscrc 配置文件](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/build-osc-config-oscrc.md)
- [跨架构打包软件为RPM包时针对具体架构的宏%ifarch](https://gitee.com/zxs-un/openEuler-port2riscv64/blob/master/doc/spec-macro-ifarch.md)

技术分享：

[包构建失败解决案例分享 2021-08-13 15:52:41  访问密码：FSaqN61o](https://meeting.tencent.com/v2/cloud-record/share?id=91a94eed-8831-4e67-9403-c4a31bc5e3a7&from=3&is-single=true)

#### 刘佳伟

PR：
[tss2适配tss2](https://gitee.com/src-openeuler/tss2)

issue
[软件包错误原因整理](https://gitee.com/openeuler/RISC-V/issues/I45G4I?from=project-issue)
[本地启动最新qemu+oe_riscv64](https://github.com/plctlab/openEuler-riscv/issues/29)

doc文档仓库：
[doc（学习、工作过程中的一些简单记录](https://gitee.com/jiawei__liu/open-euler_riscv64)
例如：
 [Ubuntu20.04 作为 QEMU RISC-V 宿主机](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/Host-Ubuntu20.04Linux.md)
[RISC-V的获取和运行](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/vm-qemu-openEuler-riscv64.md)

技术分享：

[包构建失败解决案例分享 2021-08-13 15:52:41  访问密码：FSaqN61o](https://meeting.tencent.com/v2/cloud-record/share?id=91a94eed-8831-4e67-9403-c4a31bc5e3a7&from=3&is-single=true)

#### 李诗洋

PR

[itrustee_sdk适配riscv64](https://gitee.com/src-openeuler/itrustee_sdk/pulls/7)
[efibootmgr适配riscv64](https://gitee.com/src-openeuler/efibootmgr/pulls/14)
[edac-utils适配riscv64](https://gitee.com/src-openeuler/edac-utils/pulls/6)
[qrencode适配riscv64](https://gitee.com/src-openeuler/qrencode/pulls/3)
doc

[在centOS7下安装obs客户端osc](https://gitee.com/lishiyangasdf/open-euler-r-v-learning-notes/blob/master/%E5%9C%A8centOS7%E4%B8%8B%E5%AE%89%E8%A3%85obs%E5%AE%A2%E6%88%B7%E7%AB%AFosc.md)
issue

[[构建失败] ck 和 ltrace [疑似源码本身不支持riscv架构]](https://gitee.com/openeuler/RISC-V/issues/I466NG?from=project-issue)
[[构建失败]abrt](https://gitee.com/openeuler/RISC-V/issues/I453WY?from=project-issue#git-comment-divider)

#### 孙浩翔

**issue**
[[构建失败]【已解决】python-urwid](https://gitee.com/openeuler/RISC-V/issues?label_ids=108875189&label_text=sig%2Fsig-RISC-V)
**doc-repo**
[PLCT实习笔记](https://gitee.com/maximsuen/plct-internship-notes)

#### 许志凌

1、解决构建失败包gdbus-codegen-glibmm
提交的issue：https://gitee.com/openeuler/RISC-V/issues/I45VBU?from=project-issue
提交的PR：https://gitee.com/src-openeuler/gdbus-codegen-glibmm/pulls/4

2、解决构建状态excluded的包的PR
acpid：https://gitee.com/src-openeuler/acpid/pulls/15
color-filesystem：https://gitee.com/src-openeuler/color-filesystem/pulls/8
dmidecode：https://gitee.com/src-openeuler/dmidecode/pulls/3
docker-anaconda-addon：https://gitee.com/src-openeuler/docker-anaconda-addon/pulls/3

3、个人学习笔记
gitee仓：https://gitee.com/xinminst/open-euler-riscv



#### 邹通成

PR：

[kmod-kvdo配置riscv64](https://gitee.com/src-openeuler/kmod-kvdo/pulls/10#note_6418349)
[libipt配置riscv64](https://gitee.com/src-openeuler/libipt/pulls/14)
[openblas配置riscv64](https://gitee.com/src-openeuler/openblas/pulls/8)

#### 许嘉玲

PR：

[lwip适配riscv64](https://gitee.com/src-openeuler/lwip.git)
[meclog适配riscv64](https://gitee.com/src-openeuler/mcelog.git)
[microcode_ctl适配riscv64](https://gitee.com/src-openeuler/microcode_ctl.git)

#### 颛孙宇翔   [zhuān sūn]

修复openeuler中报错excluded包，添加riscv构建，但这些包仍有新的错误，进行了错误汇总上报。
| [prefetch_tuning](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/prefetch_tuning) |
| [psm](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/psm) |
| [rear](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/rear) |
| [rpm-ostree](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/rpm-ostree) |
| [rust](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/rust) |
| [sgabios](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/sgabios) |
| [shim](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/shim) |
| [spark](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/spark) |
| [spdk](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/spdk) |
| [spice](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/spice) |
| [stratovirt](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/stratovirt) |
| [syslinux](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/syslinux) |
修复openeuler中broken包，添加_serverce文件，进行构建尝试，但这些包有新的错误，进行了错误汇总上报。
| [nodejs-clone](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/nodejs-clone) |
| [openEuler-indexhtml](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/openEuler-indexhtml) |
|[glassfish-hk2](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/glassfish-hk2)|
学习了Linux命令行基础，Git工具基础。学习了OBS构建的相关基础。

#### 马驰

错误整理
https://gitee.com/mc964203886/OpenEuler-Mainline-RISC-V-Error-Type-August
Issue
https://gitee.com/openeuler/RISC-V/issues/I45G4I?from=project-issue

#### 吴洁



#### 王俊强

bishengJDk：https://gitee.com/openeuler/RISC-V/issues/I28H7L?from=project-issue  或  https://github.com/plctlab/openEuler-riscv/issues/9

xface可视桌面支持：https://github.com/plctlab/openEuler-riscv/issues/10 

依赖仓搭建与同步：https://mirror.iscas.ac.cn/openeuler-sig-riscv/ 