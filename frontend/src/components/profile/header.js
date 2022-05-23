import {useState, useEffect, useContext} from "react"
import ProptTypes from "prop-types"; 
import Skeleton from "react-loading-skeleton";
import useUser from "../../hooks/use-user";
import { isUserFollowingProfile, toggleFollow } from "../../services/axios";
import UserContext from "../../context/user";
import { DEFAULT_IMAGE_PATH } from "../../constants/paths";


export default function Header({
    photosCount, 
    followerCount,
    setFollowerCount,
    profile:{
        docId: profileDocId, 
        userId: profileUserId, 
        fullName,
        followers, 
        following,
        username: profileUsername
    }
}){
    const {user: loggedInUser } = useContext(UserContext); 
    const { user } = useUser(loggedInUser?.uid); 
    const [isFollowingProfile, setIsFollowingProfile] = useState(null); 
    const activeBtnFollow = user?.username && user?.username !== profileUsername; 

    const handleToggleFollow = async() =>{
        //TODO: WIP
    }             

    useEffect(() =>{
        //TODO: WIP
    });

    return(
        <div className="grid grid-cols-3 gap-4 justify-between mx-auto max-w-screen-lg">

            <div className="container flex justify-center items-center">
                {profileUsername ? (
                    <img
                        className="rounded-full h-40 w-40 flex"
                        alt=""
                        src={`/images/avatars/${profileUsername}.jpg`}
                        onError={(e) =>{
                            e.target.src = DEFAULT_IMAGE_PATH;
                        }}/>
                ): (
                    <Skeleton circle height={150} width={150} count={1}/> )}
            </div>
            <div className="flex items-center justify-center flex-col col-span-2">
                <div className="container flex items-center">
                    <p className="text-2xl mr-4">{profileUsername}</p>
                    {activeBtnFollow && isFollowingProfile === null ? (
                        <Skeleton count={1} width={80} height={32}/>
                    ): (
                        activeBtnFollow && (
                            <button 
                                className="bg-blue-medium font-bold text-sm rounded text-white w-20 h-8"
                                type="button"
                                onClick={handleToggleFollow} 
                                onKeyDown={(event) =>{
                                    if(event.key === "Enter"){
                                        handleToggleFollow();
                                    }
                                }}>{isFollowingProfile ? 'Unfollow': 'Follow'}</button>
                        )
                    )}
                </div>
                <div className="container flex mt-4">
                    {!followers || ! following ?(
                        <Skeleton count={1} width={677} height={24}/>
                    ): (
                        <>
                            <p className="mr-10">
                                <span className="font-bold">{following?.length}</span> Following
                            </p>
                        </>
                    )}
                </div>
                <div className="container mt-4">
                    <p className="font-medium">{!fullName ? <Skeleton count={1} height={24} />: fullName}</p>
                </div>
            </div>
        </div>
    ); 

}

Header.propTypes = {
    photosCount: ProptTypes.number.isRequired, 
    followerCount: ProptTypes.number.isRequired, 
    setFollowerCount: ProptTypes.func.isRequired, 
    profile: ProptTypes.shape({
        docId: ProptTypes.string, 
        userId: ProptTypes.string, 
        fullName: ProptTypes.string, 
        usernam: ProptTypes.string, 
        followers: ProptTypes.array, 
        following: ProptTypes.array
    }).isRequired
};