1. 前提1：装好yarn，npm，python并设置好环境变量
2. 前提2：装好npm的create-react-app包
3. 进入应用所在目录
4. pip intstall virtualenv
5. virtualenv env
6. \env\Scripts\activate
7. pip intstall -r "requirments.txt"
8. create-react-app front
9. cd front
10. yarn start
11. 后置1：yarn build构建
12. 后置2：yarn start测试
13. 注：由于build生成的文件是在front目录下，为了后端能够用到必须在后端目录下建立templates文件夹和static文件夹并把文件移到那里，方法见14、15、16点
14. 应用目录下的back目录下建立static和templates两个文件夹
15. 在package.json的scrips添加{"preb": "cd ..\\back && rd /q /s static && del templates /q \\* && cd ..\\front",}一项
16. 在package.json的scrips添加{"postb": "cd build && move * ..\\..\\back\\templates\\ && Xcopy * ..\\..\\back /s /e /y && cd ..",}一项
17. 同上添加{"allb": "yarn preb && yarn build && yarn postb && cd .. && py app.py",}