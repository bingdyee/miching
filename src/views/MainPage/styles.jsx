import { red } from "@material-ui/core/colors";

export default theme => ({
    root: {
        width: '100%',
        height: '100%',
        
    },
    left: {
        width: '21%',
        height: 'calc(100% - 5%)',
        marginTop: '2.4%',
        marginLeft: '1%',
        position: 'fixed',
        overflow: 'hidden',
        [theme.breakpoints.down('sm')]: {
            display: 'none',
        },
    },
    searcher: {
        width: '100%',
        float: 'left',
        height: '34%',
        display: 'flex',
        marginBottom: '1%',
    }, 
    market: {
        display: 'flex',
        float: 'left',
        width: '100%',
        height: '34%',
        marginBottom: '1%',
    },
    trending: {
        display: 'flex',
        float: 'left',
        width: '100%',
        height: '30%',
    },
    mid: {
        color: 'red',
        width: '55%',
        height: 'calc(100% - 11.8%)',
        position: 'fixed',
        marginTop: '5.2%',
        marginLeft: '23%',
    },
    kline: {
        width: '100%',
        height: '64%',
        // border: '1px solid red',
        backgroundSize: '100% 100%',
        backgroundImage: `url(/assets/midtop.png)`,
    },
    kHeader: {
        height: '8%',
        color: 'red',
    },
    kBody: {
        height: '92%'
    },
    macd: {
        marginTop: '1.5%',
        height: '34%',
        border: '1px solid white',
    }
});
