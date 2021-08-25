import React,{useState} from 'react'
import { useRouter } from 'next/router'
import { Navbar, Form, Button, Container } from 'react-bootstrap'
import Logo from "../public/magnifying_glass.svg"

export default function NavLayout() {
  
  const router=useRouter()
  const [query, setQuery] = useState(router.query.query)
  const searchQuery = (e,path) => {
    e.preventDefault()
    router.push(path)
  }
  return (
    <Navbar sticky="top" expand="lg" bg="grey" >
      <Container>

        <Navbar.Brand href="/"
          className="col-lg-2 rounded border"
          style={{ "textAlign": "center", "fontWeight": "bold" }}
          title="Ana sayfaya gitmek için tıklayın">
          Param Cebimde
        </Navbar.Brand>
        
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Form className="d-flex col-lg-9" onSubmit={ (e)=>searchQuery(e,"/arama/"+query)}>
            <input
              
            type="text"
            placeholder="Ucuza bulmak istediğin nedir?"
            className="mr-2 form-control"
              aria-label="Ucuza bulmak istediğin nedir?"
              value={query}
              onChange={(e)=>setQuery(e.target.value)}
            />
            <Button  type="submit" variant="primary"><Logo/></Button>
          </Form>
          </Navbar.Collapse>
      </Container>
    </Navbar>
  )
}
