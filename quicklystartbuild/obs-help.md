### 查看自己的工程

1. 浏览器：https://build.openeuler.org/  并登录
2. 点击右上角的账号名
3. 根据project名点击进去查看project，也可以查看其下的packages。

![image-20211020114500111](images/image-20211020114500111.png)



### 查看别人的工程

1. 浏览器地址栏中通过url中输入用户账号：https://build.openeuler.org/user/show/<obs-userid>

2. 能够出现类似上图的界面，然后就可以继续查看了

3. 根据project名点击进去查看project下的packages：这里就不详述了。

   

怎么知道别人的账号？

1. 在 Tasks列表中查看所有的submit信息，可以看到提交人的账号；
2. 找到一个project，在【Repositories】中，点【Add from a Package】；在弹出框中的project栏中输入home，会出现下拉列表，列表中home：后面的大多时注册用户的userid；![image-20211020115421818](images/image-20211020115421818.png)



### 从mainline获取一个package到个人工程下

1. 浏览器访问https://build.openeuler.org/project/show/openEuler:Mainline:RISC-V  ，（可根据右侧构建状态点击进去按照包构建状态筛选）

   ![image-20211020142515868](images/image-20211020142515868.png)

2. 点击包名进入后，点击【Branch Package】将包导入到自己的obs工程下

   ![image-20211020142544801](images/image-20211020142544801.png)

   ![image-20211020142742251](images/image-20211020142742251.png)

3. 点击【Accept】





### 提交一个submit

1. 检查build状态为succeeded
2. 点击【Submit package】
3. 填写submit信息：
   - To target project: *：openEuler:Mainline:RISC-V
   - To target package:   openEuler:Mainline:RISC-V中的包名（如果没有修改过一般不用写）
   - Description: *：对包做了哪些修改，需要认真填写，方便maintainer审核，也方便后续查询和追溯变更过程；
   - **多次提交同一个包，建议要么撤回之前的修改，要么在后续提交的时，替代之前的submit；**



![image-20211020112626373](images/image-20211020112626373.png)

![image-20211020113051703](images/image-20211020113051703.png)



![image-20211020113259561](images/image-20211020113259561.png)





### 查看自己提交的submit 

![image-20211020112151108](images/image-20211020112151108.png)





### 撤回obs submit

![image-20211020112434303](images/image-20211020112434303.png)

![image-20211020112409566](images/image-20211020112409566.png)





### 审核并合并submit

**有权限的人才可操作**

![image-20211020113745155](images/image-20211020113745155.png)

![image-20211020114049752](images/image-20211020114049752.png)



查看具体的修改内容，无问题后，点【Accept request】接受submit请求，完成合并；如需拒绝可以点【Decline request】；





### 创建一个新的project

![image-20211027202630400](images/image-20211027202630400.png)

![image-20211027202713433](images/image-20211027202713433.png)





### 添加一个包-新建

1. 先进入一个project
2. 点击【Create Package】创建一个package





![image-20211027202932903](images/image-20211027202932903.png)



![image-20211027203054908](images/image-20211027203054908.png)



![image-20211027203154409](images/image-20211027203154409.png)



![image-20211027203334846](images/image-20211027203334846.png)



如果只提供文件名，则创建一个空文件(触摸)。  

src url。 RPM文件将被提取。 git存储库的url将被存储在一个tar球中。  



点击【save】后，obs会根据_service中的url和revision信息去git源码仓中拉取源文件，并自动开始build。



### 添加一个包-从别的工程中branch



![image-20211027203807451](images/image-20211027203807451.png)



### 如何创建一个rpm仓库

#### 1. 

![image-20211027203845671](images/image-20211027203845671.png)





![image-20211027204106189](images/image-20211027204106189.png)



![image-20211027204518120](images/image-20211027204518120.png)

![image-20211027204553466](images/image-20211027204553466.png)

![image-20211027204611917](images/image-20211027204611917.png)



#### 2.

![image-20211027210105736](images/image-20211027210105736.png)



![image-20211027205900787](images/image-20211027205900787.png)



### 给仓库添加依赖仓

![image-20211027204806291](images/image-20211027204806291.png)

![image-20211027204844147](images/image-20211027204844147.png)



![image-20211027204906139](images/image-20211027204906139.png)

