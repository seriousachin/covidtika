mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

file=~/.streamlit/static/index.html
sed -i 's/"<title>Streamlit</title>"/"<title>Covid Tika Tracker</title>"/g' $file