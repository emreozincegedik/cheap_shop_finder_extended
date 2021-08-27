import React from 'react'

export default function Card({img,title,price,link,website}) {
  return (
    <div  className="container d-flex flex-row card" style={{"marginTop":"1rem"}}>
      <div className="col-lg-3">
        <img alt={title || "item_title"} src={ img||"https://childrenheartcare.com/wp-content/uploads/2019/08/ASD-TYPES.jpg" } className="item_photo"/>
      </div>
      <div className="col-lg-8">
        <h3>title</h3>
        <p>price</p>
      </div>
      <div className="col-lg-1">
        <button className="btn btn-block btn-primary">asd</button>
      </div>
    </div>
  )
}
