import { NavLink } from 'react-router-dom';

export default function NavBar() {
    return (
        <>
            <div className="container mt-2 heliotrope_gray b_cards rounded shad_bottom">
                <header className="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between pt-4 mb-4">
                    <NavLink to='/' className='text-decoration-underline link-dark'>
                        <div className="d-flex align-items-center col-md-3 ms-3 mb-md-0 text-dark text-decoration-none">
                            <p className='display-2 nameText'>Impulse</p>
                        </div>
                    </NavLink>
                    <ul className="nav col-12 ms-5 col-md-auto mb-2 text-decoration-none link-dark justify-content-center siteText mb-md-0">
                        <li className="nav-item">
                            <NavLink className="nav-link text-decoration-none link-dark" aria-current="page" to="/">Home</NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className="nav-link text-decoration-none link-dark" to="subscriptions/">Subscription Boxes</NavLink>
                        </li>
                        <div className="dropdown">
                            <button className="pb-2 nav-link btn btn-toggle dropdown-toggle text-decoration-none link-dark fw-semibold"
                                type="button" id="dropdownMenuButton2" data-bs-toggle="dropdown" aria-expanded="false">
                                Products
                            </button>
                            <div className="dropdown-menu dropdown-menu-light dropdown-collapse" aria-labelledby="dropdownMenuButton2">
                                <li><NavLink className="fs-4 dropdown-item" aria-current="page" to="things/">Things</NavLink></li>
                                <li><NavLink className="fs-4 dropdown-item" aria-current="page" to="clothing/">Styles</NavLink></li>
                            </div>
                        </div>
                    </ul>
                    <div className="col-md-3 me-3 text-end">
                        <NavLink className='' to='login/'>
                            <button type="button" to='login/' className="btn ob_button me-2 almond">Login</button>
                        </NavLink>
                        <NavLink className='' to='signup/'>
                            <button type="button" className="btn ob_button almond">Sign-up</button>
                        </NavLink>
                        <NavLink className="nav-link" to="checkout/">
                            <button className='btn mt-2'>
                                <img className='' src='./sh_cart_smol.png' width="" height="20" alt="cart gone :(" />
                            </button>
                        </NavLink>
                    </div>
                </header>
            </div>
        </>
    );
};


