export interface LoginResponse {
  access_token: string
  token_type: string
  user: {
    id: number
    username: string
    name: string
    role: string
  }
}