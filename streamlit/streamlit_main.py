import subprocess
import sys

def run_streamlit(appName):
    subprocess.run([sys.executable,
                    "-m", "streamlit", "run",
                    str(appName)])

# 실행 진입점
# 위치는 파일 맨 아래
if __name__ == "__main__":
    #run_streamlit("12_streamlit_tab.py")
    #run_streamlit("13_streamlit_multi_pages.py")
    #run_streamlit("14_streamlit_multi_pages.py")
    run_streamlit("15_streamlit_query_params.py")