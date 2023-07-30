import styles from './AppNav.module.scss';
import {useAuth} from "../hooks/auth";
import React, {useEffect, useState} from "react";
import {Link, useLocation} from "react-router-dom";
import {Button} from "@mui/material";
import logout from '../hooks/auth'

const publicRoutes = [
    {
        text: 'Login',
        link: '/login',
    },
    {
        text: 'Register',
        link: '/register',
    },
];

const privateRoutes = [
    {
        text: 'Logout',
        link: '/logout',
    },
];

const AppNav = () => {
    const {isLoggedIn} = useAuth();
    const [currentRoute, setCurrentRoute] = useState(null);
    const [routes, setRoutes] = useState(publicRoutes);
    const location = useLocation();

    useEffect(() => {
        setRoutes(
            isLoggedIn
                ? privateRoutes
                : publicRoutes
        )
    }, [isLoggedIn]);

    useEffect(
        () => {
            let route = routes.find(r => r.link === location.pathname);
            if (!route) {
                route = routes[0]
            }
            setCurrentRoute(route);
        },
        [location, routes]
    );

    const renderLink = (route) => {
        if (route.link === '/logout') {
            return <Button onClick={() => logout()}>
                Logout
            </Button>
        }

        return (
            <Link to={route.link}>{route.text}</Link>
        )
    }

    return (
        <nav>
            <ul className={styles.listNav}>
                {routes.map(r => (
                    <li key={r.link} className={styles.listNavItem}>
                        {renderLink(r)}
                    </li>
                ))}
            </ul>
        </nav>
    );
};

export default AppNav;
