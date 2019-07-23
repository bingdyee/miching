import React from 'react';
import { withStyles, Typography, InputBase, Table, TableHead, TableBody, TableRow, TableCell  } from '@material-ui/core';
import SearchIcon from '@material-ui/icons/Search';
import styles from './styles';
		
		
const Records = [
    {name: '移远通信', price: 84.21, rate: '10.01%', color: 'yellow'},
    {name: '太化股份', price: 5.81, rate: '10.04%', color: 'red'},
    {name: '天坛生物', price: 24.94, rate: '6.72%', color: 'green'},
];

class Searcher extends React.PureComponent {

    render() {
        const { classes } = this.props;
        return (
            <div className={classes.root}>
                <Typography variant="h6" component="h6" className={classes.title}>股 票 检 索</Typography>
                <div className={classes.search}>
                    <div className={classes.searchIcon}><SearchIcon /></div>
                    <InputBase
                        placeholder="请输入股票名称或代码"
                        classes={{
                            root: classes.inputRoot,
                            input: classes.inputInput,
                        }}
                        inputProps={{ 'aria-label': 'Search' }}
                    />
                </div>
                <div className={classes.recommend}>
                    <Table className={classes.table} size="small">
                        <TableHead>
                            <TableRow>
                                <TableCell className={classes.cell} align="center">名称</TableCell>
                                <TableCell className={classes.cellTwo} style={{color: 'white'}} align="center">昨日价</TableCell>
                                <TableCell className={classes.cellThree} style={{color: 'white'}} align="center">涨幅率</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {
                                Records.map(record => (
                                    <TableRow key={record.name}>
                                        <TableCell style={{color: record.color}} align="center">{record.name}</TableCell>
                                        <TableCell className={classes.cellTwo} style={{color: record.color}} align="center">{record.price}</TableCell>
                                        <TableCell className={classes.cellThree} style={{color: record.color}} align="center">{record.rate}</TableCell>
                                    </TableRow>
                                ))
                            }
                        </TableBody>
                    </Table>
                </div>
            </div>
        )
    }

}

export default withStyles(styles)(Searcher);