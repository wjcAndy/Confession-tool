告白神器支持文字修改

一键打包命令，支持手机、电脑

调整文字坐标

##mac打包命令

nuitka --standalone --onefile --macos-create-app-bundle --output-dir=dist --remove-output --include-data-file="文字消除版可以.png=文字消除版可以.png" --include-data-file="比心.png=比心.png" 表白.py

##win打包命令
nuitka --standalone  --onefile  --windows-disable-console --output-dir=dist --remove-output --include-data-file="文字消除版可以.png=文字消除版可以.png"   --include-data-file="比心.png=比心.png"  表白.py


nuitka --standalone \
        --onefile \
        --windows-disable-console \
        --output-dir=dist \
        --remove-output \
        --include-data-file="文字消除版可以.png=文字消除版可以.png" \
        --include-data-file="比心.png=比心.png" \
        表白.py
