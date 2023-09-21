import streamlit as st
import requests

url = "https://api.nasa.gov/planetary/apod?api_key=4N9NifiTKzTUpnyHQlisrZMSFed5ua8N9VA5YzUd"

# Get the request data as a dictionary
request = requests.get(url)
content = request.json()

#  Get the image url from the request dictionary
image_url = content['url']
request_image_url = requests.get(image_url)

# Download the image
with open("image.jpg", "wb") as file:
    image = file.write(request_image_url.content)


#  Render the image 
st.title(content['title'])
st.image("image.jpg")
st.write(content['explanation'])
