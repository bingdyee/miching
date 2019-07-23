import { fade } from '@material-ui/core/styles';

export default theme => ({
    root: {
        height: '100%',
        width: '100%',
        backgroundImage: `url(/assets/boxbg.png)`,
        backgroundSize: '100% 100%',
        overflow: 'hidden',
    },
    title: {
        marginTop: '0.6rem',
        height: '8%',
        backgroundImage: `url(/assets/stitlebg.png)`,
        backgroundSize: '100% 100%',
        fontSize: '1vw',
        fontWeight: 'bold',
        textAlign: 'center'
    },
    search: {
        height: '16%',
        position: 'relative',
        borderRadius: theme.shape.borderRadius,
        border: '1px solid #80ffff',
        width: '86%',
        marginTop: '3%',
        margin: '0 auto',
        '&:hover': {
            backgroundColor: fade(theme.palette.common.white, 0.15)
        },
    },
    searchIcon: {
        width: theme.spacing(8),
        height: '100%',
        position: 'absolute',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        float: 'left',
        width: '20%',
        cursor: 'pointer',
        color: '#80ffff'
    },
    inputRoot: {
        height: '100%',
        color: 'inherit',
        width: '80%',
        marginLeft: '19%',
    },
    inputInput: {
        color: '#80eeee'
    },
    recommend: {
        height: '62%',
        width: '86%',
        marginTop: '3%',
        margin: '0 auto',
    },
    table: {
        height: '92%',
    },
    cell: {
        color: 'white',
    },
    cellTwo: {
        [theme.breakpoints.down('sm')]: {
            display: 'none'
        },
    },
    cellThree: {
        [theme.breakpoints.down('sm')]: {
            display: 'none'
        },
        [theme.breakpoints.down('md')]: {
            display: 'none'
        },
    }
});