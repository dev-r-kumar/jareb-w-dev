import "../styles/TypingIndigator.css";
import { useEffect, useRef } from "react";
import audioFile from "./audio.mp3";

function TypingIndigator({ Indigator })

{
    const audioRef = useRef();

    let audio = new Audio("./audio.mp3");

    useEffect(() => {
        if (Indigator)
        {
            audioRef.current.currentTime = audioRef.current.duration / 2;
            audioRef.current.play();
        }
    }, [Indigator])

    return (
        <div id="iHolder">
            <div class={`wrapper ${Indigator ? "show" : "hide"}`} id="responseOnWayIndigator">
                <div class="container" >
                    <div class=" bubble two">
                        <p id="typing">Typing</p>
                        <div class="tile"></div>
                        <div class="tile"></div>
                        <div class="tile"></div>
                    </div>
                </div>
                </div>
                <audio ref={audioRef} src={audioFile} />
        </div>
    )
}

export default TypingIndigator;