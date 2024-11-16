package dto

type User struct {
    userId string
    roles []string
    permissions []string
}

func NewUser(userId string, roles, permissions []string) *User {
    return &User{userId, roles, permissions}
}

func (user *User) GetUserId() string {
    return user.userId
}

func (user *User) GetRoles() *[]string {
    return &user.roles
}

func (user *User) GetPermissions() *[]string {
    return &user.permissions
}


