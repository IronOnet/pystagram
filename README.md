# pystagram
    An instagram API built with djangorestframework

## System design
### What is Instagram?

#### Functional requirements
        => Instagram is a photo-sharing & recently video where users can upload photos and videos
        to share with other users. 

        => Users can share photos and videos with their followers 
        => Users can follow each other 
        => Users can like or dislike other user's posts 
        => Users can post stories 
                - a story can last 24 hours 
        => Users can create a collection of stories 
        => Users can comment on posts 
        => The system generates a news feed for each user containing 100 posts 
        => A post can contain multiple images or videos 
        => Users can add a tag to a post 
        => Users can search 

#### Non functional requirements

        => Our service needs to be highly reliable 
        => The acceptable latency of the system is 200ms for news feed generation 
        => Consistency can take a hit (in the interest of availability), if a user doesn't see a 
        photo for a while, it should be fine

##### Not in scope:

        => Adding tags to photos, searching photos on tags, commenting on photos, tagging users to photos