import React from 'react'
import { useRouter } from 'next/router'

export default function Page() {
  const router = useRouter()
  const { page } = router.query
  return (
    <div>
      Arama sayfa: {page}
    </div>
  )
}
