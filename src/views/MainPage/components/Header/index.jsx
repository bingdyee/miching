import React from 'react';
import { withStyles, Box, Typography } from '@material-ui/core';
import styles from './styles';

function Header(props) {
    const { classes } = props;
    return (
        <Box className={classes.root}>
            <Typography variant="h4" className={classes.title}>股 票 行 情 分 析</Typography>
        </Box>
    )
}

export default withStyles(styles)(Header);
