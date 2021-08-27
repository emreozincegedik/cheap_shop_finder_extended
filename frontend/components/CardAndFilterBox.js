import React from 'react'
import Filter from './Filter'
import Card from "./Card"

export default function CardAndFilterBox(props) {
  return (
    <div className="container d-flex flex-row">
      
        <Filter/>


      <div className="col-lg-9">
        {[1,2,3,4,5,6].map(card=><Card/>)}
      </div>
    </div>
  )
}
