import React,{useState,useEffect} from 'react'
import Filter from './Filter'
import Card from "./Card"
import Pagination from './Pagination'
import Spinner from "./Spinner"
import { useRouter } from 'next/router'

export default function CardAndFilterBox(props) {
  const router = useRouter()
  const { query, page } = router.query
  const [items, setItems] = useState([])
  const [search, setsearch] = useState(true)
  const body={
          query: query,
          page: page || 1
  }
  useEffect(() => {
    setsearch(true)
    setItems([])
    fetch("/api",
      {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        // mode: 'cors', // no-cors, *cors, same-origin
        // cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        // credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json'
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: JSON.stringify(body)
      }
    )
      .then(res => res.json())
      .then(json => {
        console.log(json)
        setItems(json.page)
        setsearch(false)
      })
    .catch(err=>console.log(err))

  }, [])
  if (search) {
    return <Spinner/>
  }
  return (
    <>
    <div className="container d-flex flex-row">
      
        <Filter/>


      <div className="col-lg-9">
          { items.map((item, i) => <Card key={i} img={item.img} title={item.title} price={item.price} link={item.link} website={item.website} />)}
      </div>
    </div>
    <Pagination/>
    </>
  )
}

