import React, {useState, useEffect} from "react";
import axio from "axios";


const baseURL = "http://127.0.0.1:8000/api/"

function login(){
    const [ post, setPost ] = useState(null);
    
    useEffect(() => {
        axios.get(baseURL).then((response) => {
            setPost(response.data);
        });
    }, []);

    if (!post) return null;

    return
    <>
    <div>
        <h1>{post.title}</h1>
        <p>{post.body}</p>
    </div>
    </>
}
export default login