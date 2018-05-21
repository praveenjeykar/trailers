#!/usr/bin/env python
import webbrowser
import os
import re
print("Content-type:text/html \n")
# Styles and scripting for the page
main_page_head = '''
<!DOCKTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="extra.css">
<div class="center"><h2>Trailers</h2>
</div>
<div class="container">

<div id="myModal" class="modal">
<div class="modal-content">
<span class="close">&times;</span>
<iframe width="400" height="300" {movie_tiles} src="https://www.w3schools.com"
frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

</div>
</div>
<script>
    var modal=document.getElementById('myModal');
    var span=document.getElementsByClassName("close")[0];
    onc=function (c){
        modal.style.display="block";
        document.getElementsByTagName("iframe")[0].setAttribute("src",'https://www.youtube.com/embed/'+c);
}
span.onclick=function(){
    modal.style.display="none";
}
window.onclick=function(event){
    if(event.target==modal){
    modal.style.display="none";
}
}
</script>
</head>
'''
# The main page layout and title bar
main_page_content = '''
<body>

<div class="box f1" onclick="onc('eoJxaz3VtuE')">

<img src="https://bit.ly/2kazWmh" alt="fig1" vspace="25" hspace="25"
style="width:50%" height=250px >
<figcaption><a href="https://en.wikipedia.org/wiki/Blue_rose">Blue Roses</a>

</div>
<div class="box f2" onclick="onc('Egjmby3wayQ')">

<img src="https://bit.ly/2IWI1ZP" alt="fig2" vspace="25" hspace="25"
style="width:50%" height=250px>
<figcaption><a href="https://en.wikipedia.org/wiki/Kingfisher">Kingfishers</a>

</div>
<div class="box f3" onclick="onc('CKMNMsRaWLI')">

<img src="https://bit.ly/2Iyg0IF" alt="fig3" alt="fig3" vspace="25" hspace="25"
style="width:50%" height=250px>
<figcaption><a href="https://en.wikipedia.org/wiki/Pet">Pets</a>

</div>
<div class="box f4" onclick="onc('XcQqm7LNRFY')">

<img src="https://bit.ly/2LgVo5m" alt="fig4"vspace="25" hspace="25"
style="width:50%"height=250px >
<figcaption><a href="https://en.wikipedia.org/wiki/Rabbit">Rabbits</a>

</div>
</body>
</html>
'''
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center"
data-trailer-youtube-id="{trailer_youtube_id}"
data-toggle="modal" data-target="#trailer">
<img src="{poster_image_url}" width="220" height="342">
<h2 style="color:white;">{movie_title}</h2>
</div>
'''



def create_movie_title_content(movies):
    # The HTML content for this section of the page
    content = ''
    a = "movie.trailer_youtube_url"
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', a)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', a)
        trailer_youtube_id = (youtube_id_match.group(0)
                              if youtube_id_match else None)
        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id)
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
	    movie_tiles=create_movie_title_content(movies))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    # open the output file in the browser(in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
