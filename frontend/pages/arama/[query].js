import React from 'react'
import { useRouter } from 'next/router'

export default function Query() {
  const router = useRouter()
  const { query } = router.query
  return (
    <div>
      Arama: {query}
    </div>
  )
}
