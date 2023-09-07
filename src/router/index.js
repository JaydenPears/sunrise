import Home from "../pages/Home";
import PageOne from "../pages/PageOne";
import PageTwo from "../pages/PageTwo";
import PageThree from "../pages/PageThree";
import PageCTA from "../pages/PageCTA";


export const arrayRoutes = [
    {id: 0, path: "", element: <Home/>, exact: true},
    {id: 1, path: "/page_one", element: <PageOne/>, exact: true},
    {id: 2, path: "/page_two", element: <PageTwo/>, exact: true},
    {id: 3, path: "/page_three", element: <PageThree/>, exact: true},
    {id: 4, path: "/page_cta", element: <PageCTA/>, exact: true},
]