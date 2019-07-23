
export default theme => ({
    root: {
        display: 'flex',
        flexGrow: 1,
        backgroundSize: '100% 100%',
        backgroundImage: `url(/assets/header.jpg)`,
        height: '10%',
        position: 'fixed',
        width: '100%',
        zIndex: -1,
        [theme.breakpoints.down('sm')]: {
            backgroundImage: 'none'
        }
    },
    title: {
        height: '100%',
        marginTop: '0.5%',
        fontSize: '2.6vw',
        fontWeight: 'bold',
        margin: '0 auto',
    }
});