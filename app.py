import streamlit as st

st.title("Titulo to guapo")

st.html("""
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vel nisi et nisi tristique convallis aliquet a sapien. Nulla non interdum nibh, <mark>eleifend tristique ligula. Nullam dictum nunc eget rutrum ornare</mark>. Curabitur ut orci lobortis, tempor nibh vitae, ornare sem. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque pretium nulla vel diam vehicula, ut euismod risus elementum. Nunc consectetur nisi vel lorem rhoncus vestibulum. Pellentesque efficitur pellentesque ipsum, in rhoncus nisl tempus et.</p>
        <style>mark {
                background-color: yellow;
                }
        
        </style>
        """)
if st.button("globos"):
    st.balloons()
if st.button("nieve"):
    st.snow()
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Happy_Shrek_%28cropped%29.jpg/320px-Happy_Shrek_%28cropped%29.jpg" )
st.html("""
    <img src="file:///image.png}" class="banner"> 
        <style> .banner{
            width= 100%
            height= 10%
            }</style>
        """)
st.link_button("repositorio")