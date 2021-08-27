import React from 'react'
import styles from '../styles/card.module.css'
import { useRouter } from 'next/router'

export default function Card({ img, title, price, link, website }) {
  const router=useRouter()
  return (
    <div  className={styles.container + " container d-flex flex-row card"}>
      <div className="col-lg-2">
        <img alt={title || "item_title"}
          src={img || "https://via.placeholder.com/250x250"}
          className={styles.item_photo} />
      </div>
      <div className={styles.nonImg+" col-lg-10 d-flex flex-column justify-content-around"}>
        <h3 className={styles.title}>{title || "title"}</h3>
        <div className="container d-flex flex-row align-self-center">

          <h4 className={styles.price+" col-lg-6"}>{price || "price"}</h4>
          <h4 className={" col-lg-6"}>TL</h4>
        </div>
        <button className={"btn btn-block btn-outline-primary " + styles.button}
          onClick={() => {
            console.log((link || "asd"))
            router.push((link || "/"))
          }}>{website || "website"}</button>
      </div>
    </div>
  )
}
