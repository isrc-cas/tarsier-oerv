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

- [包构建失败解决案例分享 2021-08-13 15:52:41  访问密码：FSaqN61o](https://meeting.tencent.com/v2/cloud-record/share?id=91a94eed-8831-4e67-9403-c4a31bc5e3a7&from=3&is-single=true)



#### 刘佳伟

PR：

- [tss2适配tss2](https://gitee.com/src-openeuler/tss2)

issue

- [软件包错误原因整理](https://gitee.com/openeuler/RISC-V/issues/I45G4I?from=project-issue)
- [本地启动最新qemu+oe_riscv64](https://github.com/plctlab/openEuler-riscv/issues/29)

doc文档仓库：

- [Ubuntu20.04作为QEMU+OE_RV的宿主机](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/Host-Ubuntu20.04Linux.md)
- [本地构建OSC](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/build-osc-build-tools.md)
- [openEuler RISC-V的获取和运行](https://gitee.com/jiawei__liu/open-euler_riscv64/blob/master/doc/vm-qemu-openEuler-riscv64.md)

技术分享：

- [包构建失败解决案例分享 2021-08-13 15:52:41  访问密码：FSaqN61o](https://meeting.tencent.com/v2/cloud-record/share?id=91a94eed-8831-4e67-9403-c4a31bc5e3a7&from=3&is-single=true)



#### 李诗洋

PR

- [itrustee_sdk适配riscv64](https://gitee.com/src-openeuler/itrustee_sdk/pulls/7)

- [efibootmgr适配riscv64](https://gitee.com/src-openeuler/efibootmgr/pulls/14)

- [edac-utils适配riscv64](https://gitee.com/src-openeuler/edac-utils/pulls/6)

- [qrencode适配riscv64](https://gitee.com/src-openeuler/qrencode/pulls/3)

doc

- [在centOS7下安装obs客户端osc](https://gitee.com/lishiyangasdf/open-euler-r-v-learning-notes/blob/master/%E5%9C%A8centOS7%E4%B8%8B%E5%AE%89%E8%A3%85obs%E5%AE%A2%E6%88%B7%E7%AB%AFosc.md)

issue

- [[构建失败] ck 和 ltrace [疑似源码本身不支持riscv架构]](https://gitee.com/openeuler/RISC-V/issues/I466NG?from=project-issue)
- [[构建失败]abrt](https://gitee.com/openeuler/RISC-V/issues/I453WY?from=project-issue#git-comment-divider)



#### 孙浩翔

issue

- [[构建失败]【已解决】python-urwid](https://gitee.com/openeuler/RISC-V/issues?label_ids=108875189&label_text=sig%2Fsig-RISC-V)

doc-repo

- [PLCT实习笔记](https://gitee.com/maximsuen/plct-internship-notes)



#### 许志凌

1、解决构建失败包gdbus-codegen-glibmm

- 提交的issue：https://gitee.com/openeuler/RISC-V/issues/I45VBU?from=project-issue
- 提交的PR：https://gitee.com/src-openeuler/gdbus-codegen-glibmm/pulls/4

2、解决构建状态excluded的包的PR

- acpid：https://gitee.com/src-openeuler/acpid/pulls/15
- color-filesystem：https://gitee.com/src-openeuler/color-filesystem/pulls/8
- dmidecode：https://gitee.com/src-openeuler/dmidecode/pulls/3
- docker-anaconda-addon：https://gitee.com/src-openeuler/docker-anaconda-addon/pulls/3

3、个人学习笔记

- gitee仓：https://gitee.com/xinminst/open-euler-riscv



#### 邹通成

PR：

- [kmod-kvdo配置riscv64](https://gitee.com/src-openeuler/kmod-kvdo/pulls/10#note_6418349)
- [libipt配置riscv64](https://gitee.com/src-openeuler/libipt/pulls/14)
- [openblas配置riscv64](https://gitee.com/src-openeuler/openblas/pulls/8)

#### 许嘉玲

PR：

- [lwip适配riscv64](https://gitee.com/src-openeuler/lwip.git)
- [meclog适配riscv64](https://gitee.com/src-openeuler/mcelog.git)
- [microcode_ctl适配riscv64](https://gitee.com/src-openeuler/microcode_ctl.git)

#### 颛孙宇翔   [zhuān sūn]

1、修复openeuler中报错excluded包，添加riscv构建，但这些包仍有新的错误，进行了错误汇总上报。

- [prefetch_tuning](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/prefetch_tuning)
- [psm](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/psm)
- [rear](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/rear)
- [rpm-ostree](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/rpm-ostree)
- [rust](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/rust)
- [sgabios](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/sgabios)
- [shim](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/shim)
- [spark](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/spark)
- [spdk](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/spdk)
- [spice](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/spice)
- [stratovirt](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/stratovirt)
- [syslinux](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/syslinux)

2、修复openeuler中broken包，添加_serverce文件，进行构建尝试，但这些包有新的错误，进行了错误汇总上报。

- [nodejs-clone](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/nodejs-clone)
- [openEuler-indexhtml](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/openEuler-indexhtml)
- [glassfish-hk2](https://build.openeuler.org/package/show/openEuler:Mainline:RISC-V/glassfish-hk2)

3、学习了Linux命令行基础，Git工具基础。学习了OBS构建的相关基础。

#### 马驰

错误整理

- https://gitee.com/mc964203886/OpenEuler-Mainline-RISC-V-Error-Type-August

Issue

- https://gitee.com/openeuler/RISC-V/issues/I45G4I?from=project-issue



#### 王俊强

- bishengJDk：https://gitee.com/openeuler/RISC-V/issues/I28H7L?from=project-issue  或  https://github.com/plctlab/openEuler-riscv/issues/9

- xface可视桌面支持：https://github.com/plctlab/openEuler-riscv/issues/10 

- 依赖仓搭建与同步：https://mirror.iscas.ac.cn/openeuler-sig-riscv/ 