import { axios } from "axios"; 

export async function doesUsernameExists(username){

}

export async function getUserByUsername(username){

}

export async function getUserByUserId(userId){

}

// check all conditions before limit results
export async function getSuggestedProfiles(userId, following){

}

export async function updateLoggedInUserFollowing(
    loggedInUserDocId, 
    profileId, 
    isFollowingProfile
){

}

export async function updateFollowedUserFollowers(
    profileDocId, 
    loggedInUserDocId, 
    isFollowingProfile
){

}

export async function getPhotos(userId, following){

}

export async function getUserPhotosByUserId(userId){
    
}

export async function isUserFollowingProfile(loggedIndUsername, profileUserId){

}

export async function toggleFollow(
    isFollowingProfile, 
    activeUserDocId, 
    profileDocId, 
    profileUserId, 
    followingUserId
){
    
}