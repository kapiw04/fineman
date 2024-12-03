package dao

import (
	"context"
	"fmt"
	"strings"

	pg "github.com/jackc/pgx/v5/pgxpool"
)

var dbConnPool *pg.Pool;
var dbString string;
type Dao struct {
    pool *pg.Pool
}

func InitDao(dbConnString string) (*Dao, error) {
    pool, err := pg.New(context.TODO(), dbConnString)
    if err != nil {
        return nil, err
    }
    return &Dao{pool}, nil
}

func toAnyArray[T any](arr []T) []any {
    res := make([]any, len(arr))
    for i, el := range arr {
        res[i] = el
    }
    return res
}

func (dao *Dao) deleteAliasesByProductGroups(ctx context.Context, productGroupIds []uint64) {
    if len(productGroupIds) == 0 {
        return
    }

    sql := `DELETE FROM "aliases" 
            WHERE product_group_id = ANY ($1) 
            RETURNING product_group_id;`
    rows, _ := dao.pool.Query(ctx, sql, productGroupIds)

    defer rows.Close()
    for rows.Next() {
        var productGroupId uint64
        err := rows.Scan(&productGroupId)
    }
}

func f(ctx context.Context, pool *pg.Pool) (err error) {
    tx, err := pool.Begin(ctx)
    if err != nil {
        return err
    }
    defer func() {
        if err != nil {
            tx.Rollback(ctx)
        } else {
            tx.Commit(ctx)
        }
    }()

    _, err = tx.Exec(ctx, "insert into users (email) values ($1)", "c@em.com")
    if err != nil {
        return err
    }

    var id int
    row := tx.QueryRow(ctx, "select id from users where email = $1", "c@em.com")
    if err := row.Scan(&id); err != nil {
        return err
    }

    // NOTE: the above is just an example, if you need the auto
    // generated id of an inserted record, please use the RETURNING
    // clause supported by PostgreSQL.
    return nil
}

