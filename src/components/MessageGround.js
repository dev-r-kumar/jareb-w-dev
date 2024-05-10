import "../styles/MessageGround.css";
import { useEffect } from "react";
import { useState } from "react";


function MessageGround({ setMessageContent })
{

    return (
        <div className="MessageGround">
            
        {
            setMessageContent.map((message) => (
                message.type === "user" ? (
                    <div className="message own" key={message.id}>
                    
                        <div class="flex items-start gap-2.5" id="userChat">
                           
                            <div class="flex flex-col gap-1 max-w-[290px]">
                                <div class="flex items-center space-x-2 rtl:space-x-reverse" id="user_chat_info">
                                </div>
                                <div class="flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-tl-xl  rounded-br-xl rounded-es-xl dark:bg-blue-600">
                                    <p class="text-sm font-normal text-gray-900 dark:text-white">{message.content}</p>
                                </div>
                            </div>
                        </div>

                    </div>
                ):(
                    <div className="message" key={message.id}>            
                        {/* bot */}
                        <div class="flex items-start gap-2.5" id="botChat">
                        <div class="w-8 h-8 rounded-full" id="miniPic" alt="Jese image"></div>
                        <div class="flex flex-col gap-1 max-w-[290px]">
                            <div class="flex items-center space-x-2 rtl:space-x-reverse">
                                <span class="text-sm font-semibold text-gray-900 dark:text-white">Jareb</span>
                                {/* <span class="text-sm font-normal text-gray-500 dark:text-gray-400">11:46</span> */}
                            </div>
                            <div class="flex flex-col leading-1.5 p-4 border-gray-200 bg-gray-100  rounded-e-xl rounded-es-xl dark:bg-blue-600">
                                <p class="text-sm font-normal text-gray-900 dark:text-white">{message.content}</p>
                            </div>
                            
                        </div>
                        </div>

                    </div>
                )
            ))
        }


        </div>
    )
}




export default MessageGround;