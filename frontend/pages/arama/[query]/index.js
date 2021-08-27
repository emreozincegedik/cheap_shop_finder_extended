import React from 'react'
import { useRouter } from 'next/router'

import CardAndFilterBox from '../../../components/CardAndFilterBox'
import Pagination from '../../../components/Pagination'

export default function Query() {
  const router = useRouter()
  const { query } = router.query
  return (
    <>
      Arama: {query}
      <CardAndFilterBox />
      <Pagination/>
    </>
  )
}
