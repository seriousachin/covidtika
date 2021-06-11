mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
#Old="<title>Streamlit</title>"
#New="<title>Covid Tika Tracker</title>"
#file=~/.streamlit/static/index.html
sed -i "s/Streamlit/CovidTikaTracker/g" ~/.streamlit/static/index.html