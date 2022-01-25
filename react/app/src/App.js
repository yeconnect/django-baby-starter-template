import React, { useState } from "react";

const MESSAGE_ENDPOINT = "http://localhost:4989/message";

const App = () => {
  const [message, setMessage] = useState("");
  const [name, setName] = useState("");

  /** バックエンドを叩いて、メッセージを取得する(django/bookstore/views.pyへ) */
  const getMessage = () => {
    fetch(MESSAGE_ENDPOINT, {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        setMessage(data.message)
      })
      .catch((error) => {
        alert('エラーが発生しました！！！')
      });
  };
  /** バックエンドを叩いて、名前を送信する(django/bookstore/views.pyへ) */
  const postMessage = () => {

    const body = new URLSearchParams()
    body.append('name', name)

    fetch(MESSAGE_ENDPOINT, {
      method: "POST",
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
      },
      body: body
    })
      .then((response) => response.json())
      .then((data) => {
        console.table(data)
      })
      .catch((error) => {
        alert('エラーが発生しました！！！')
      });
  };

  return (
    <div>
      <button onClick={getMessage}>APIをGETで叩く</button>
      <p>バックエンドからのメッセージ→{message}</p>

      <hr />
      <button onClick={postMessage}>APIをPOSTで叩く</button>
      <input value={name} onChange={(e)=>{setName(e.target.value)}}/>
    </div>
  );
};

export default App;
