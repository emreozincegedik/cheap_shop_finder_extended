import React from 'react'
import { useRouter } from 'next/router'

import CardAndFilterBox from '../../../components/CardAndFilterBox'

export default function Page() {
  const router = useRouter()
  const { page } = router.query
  return (
    <>
      Arama sayfa: {page}
      <CardAndFilterBox />
    </>
  )
}
