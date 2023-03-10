import React from 'react'
import { NavLink } from 'react-router-dom'
import { useToken, useAuthContext } from './auth';

export default function LoginSignUpLogout() {
    const [, logout] = useToken();
    const { token } = useAuthContext();

    const goodbye = async e => {
        e.preventDefault();
        await logout();
        console.log("Logged out");
    }

    if (token) {
        return (
            <>
                <div className="col-md-3 me-2 text-end">
                    <button onClick={goodbye} type="button" className="btn ob_button almond">Logout</button>
                </div>
            </>
        )
    } else {
        return (
            <>
                <div className="col-md-3 me-2 text-end">
                    <NavLink className='link-dark' to='login/'>
                        <button type="button" to='login/' className="btn ob_button me-2 almond">Login</button>
                    </NavLink>
                    <NavLink className='link-dark' to='signup/'>
                        <button type="button" className="btn ob_button almond">Sign-up</button>
                    </NavLink>
                </div>
            </>
        );
    };
};
