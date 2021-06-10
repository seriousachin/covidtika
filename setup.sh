mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml

#file=~/.streamlit/static/index.html
#sed -i 's/<title>Streamlit</<title>Covid Tika Tracker</g' $file