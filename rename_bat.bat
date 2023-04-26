
rem 2021 1222 
rem 任意のディレクトリの入力受付
set user_input_str = 
set /p user_input_str = "任意のファイルを入力してね："

rem コピー処理
for %%i in ("") do (
cp user_input_str Y:\blenderProjects\Tempa
)