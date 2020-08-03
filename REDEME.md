### 该系统为Python3.8+Django3.0实现的商城后台管理系统

### 该系统实现了自定义登录、自定义注册、自定义认证、自定义权限、通用工具类、一般实体类的增删查改操作,同时配置sentry进行系统监控

* 登录
1.单点登录
2.自定义登录接口类

* 注册
1.自定义注册接口类

* 认证
1.采用JWT认证
2.采用OAuth2认证

* 权限
1.单个接口权限管控
2.全局管控

* 其他
1.自定义返回数据格式
2.自定义统一的成功、错误、警告提示



### 默认登录用户名密码
{
	"username":"admin",
	"password":"admin123"
}

#### 设置登录白名单，在名单内的接口不需要登录
1.编写中间件，过滤掉白名单内的接口