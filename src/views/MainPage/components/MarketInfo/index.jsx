import React from 'react';
import { withStyles, Typography, Table, TableBody, TableRow, TableCell  } from '@material-ui/core';
import styles from './styles';


const data = [
    {one: '昨日: 172.90 ', two: '均价：174.50', colorOne: 'red', colorTwo: 'green', rowStyle: ''},
    {one: '涨跌：0.190', two: '今开：174.81', colorOne: 'pink', colorTwo: 'green'},
    {one: '涨幅：0.11%', two: '最高：175.23', colorOne: 'yellow', colorTwo: 'pink'},
    {one: '换手：0.52%', two: '最低：172.59', colorOne: 'white', colorTwo: 'red'},
    {one: '总量：1365w', two: '量比：0.76', colorOne: 'red', colorTwo: 'orange'},
    {one: '外盘：682.7w', two: '内盘：682.0w', colorOne: 'gray', colorTwo: 'green'},
];

class MarketInfo extends React.PureComponent {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.root}>
               <Typography variant="h6" className={classes.title}>行 情 报 价</Typography>
               <Table className={classes.data} size="small">
                   <TableBody> 
                    {
                        data.map(dt => (
                            <TableRow key={dt.one}>
                                <TableCell style={{color: dt.colorOne}} align="center">{dt.one}</TableCell>
                                <TableCell style={{color: dt.colorTwo}} align="center">{dt.two}</TableCell>
                            </TableRow>
                        ))
                    }
                    </TableBody>
               </Table>
            </div>
        )
    }

}

export default withStyles(styles)(MarketInfo);