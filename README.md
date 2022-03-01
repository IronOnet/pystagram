# pystagram
    An instagram (clone) API built with djangorestframework

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

##### **Not in scope:**

        => Adding tags to photos, searching photos on tags, commenting on photos, tagging users to photos
        
#### Some design considerations

        => Practically users can upload as many photos as they like. Efficient managment of storage should be a crucial factor while designing this system 

        => Low latency is expected while viewing photos 
        => Data should be 100% reliable. If a user uploads a photo, the system will guarantee that it will never be lost. 

#### Capacity Estimation and constraints 

        * let's assume we have 100M total users, with 1M daily active users 
        * 2M new photos every day, 23 new photos every second. 
        * Average photo file size => 200kb 
        * Total space required for 1 day of photos 

                2M * 200kb => 400GB

        * Total space required for 5 years: 

                400GB * 365 * 5 (years)  ~= 730TB


#### High level system design 

            
<p align="center">
        <img src="assets/high_level_design.png">
        <br/>
</p>

#### Data model 

        * Post: 
            - userId: int 
            - media_url: varchar(256)
            - media_longitude: int 
            - media_latitude : int 
            - user_longitude: int 
            - user_latitude: int
            - comments: fk
            - created_at: timestamp 
            - updated_at: timestamp 

        * Comment: 
            - user_id: fk 
            - comment_id: int 
            - text: varchar(256)
            - replies: self  

        * Users: 
            - username : varchar(30) 
            - name: varchar(256) 
            - email: varchar(256) 
            - password: varchar(256)
            - birth_date: datetime 
            - last_login: datetime


        * Following: 
            - from : fk (user_id)
            - to: fk (user_id)  

        * Tag
          - title 

        * Tag_Photo
           - tag_id 
           - post_id 

        * Likes
          * user_id 
          * type
          * timestamp
          * post_id

        * Location: 
          * id 
          * name (varchar 200)
          * shortname (varchar 50)
         



## Detailed System design 

        - uploading photos and images can be a slow process as opposed to reads,
         normally in real world scenarios we will have to implement two services
         one to deal with reads and the other writes but for the sake of shortness we
         will bundle both services in a monolith we can even add a task queue between the database and the api server to handle upload tasks

<p align="center">
        <img src="assets/detailed_system_design.png">
        <br/>
</p>


## Detailed System design



