import numpy as np

class Vol:
    def __init__(self, sx, sy, depth, c):
        self.sx = sx
        self.sy = sy
        self.depth = depth
        self.w = np.zeros(sx*sy*depth)
        self.dw = np.zeros(sx*sy*depth)
        self.reset(c)

    def reset(self, c):
        for i in range(len(self.w)):
            self.w[i] = np.random.randn()*c

    def get_grad(self, x, y, d):
        return self.dw[((self.sx * y)+x)*self.depth+d]

    def set_grad(self, x, y, d, v):
        self.dw[((self.sx * y)+x)*self.depth+d] = v

    def set(self, x, y, d, v):
        self.w[((self.sx * y)+x)*self.depth+d] = v

    def get(self, x, y, d):
        if x>=0 and x<self.sx and y>=0 and y<self.sy and d>=0 and d<self.depth:
            return self.w[((self.sx * y)+x)*self.depth+d]
        return 0.0

    def add_grad(self, x, y, d, v):
        self.dw[((self.sx * y)+x)*self.depth+d] += v

    def toJSON(self):
        return {'sx': self.sx, 'sy': self.sy, 'depth': self.depth, 'w': self.w.tolist()}

    def fromJSON(self, json):
        self.sx = json['sx']
        self.sy = json['sy']
        self.depth = json['depth']
        self.w = np.array(json['w'])

class ConvLayer:
    def __init__(self, opt):
        opt = opt or {}
        self.out_depth = opt['filters']
        self.sx = opt['sx']
        self.in_depth = opt['in_depth']
        self.in_sx = opt['in_sx']
        self.in_sy = opt['in_sy']
        self.sy = opt['sy'] if 'sy' in opt else self.sx
        self.stride = opt['stride'] if 'stride' in opt else 1
        self.pad = opt['pad'] if 'pad' in opt else 0
        self.l1_decay_mul = opt['l1_decay_mul'] if 'l1_decay_mul' in opt else 0.0
        self.l2_decay_mul = opt['l2_decay_mul'] if 'l2_decay_mul' in opt else 1.0
        self.out_sx = int((self.in_sx + self.pad * 2 - self.sx) / self.stride + 1)
        self.out_sy = int((self.in_sy + self.pad * 2 - self.sy) / self.stride + 1)
        self.layer_type = 'conv'
        bias = opt['bias_pref'] if 'bias_pref' in opt else 0.0
        self.filters = [Vol(self.sx, self.sy, self.in_depth) for i in range(self.out_depth)]
        self.biases = Vol(1, 1, self.out_depth, bias)

    def forward(self, V):
        self.in_act = V
        A = Vol(self.out_sx, self.out_sy, self.out_depth, 0.0)
        V_sx = V.sx
        V_sy = V.sy
        xy_stride = self.stride
        for d in range(self.out_depth):
            f = self.filters[d]
            x = -self.pad
            y = -self.pad
            for ay in range(self.out_sy):
                y = -self.pad
                for ax in range(self.out_sx):
                    a = 0.0
                    for fy in range(f.sy):
                        oy = y + fy
                        for fx in range(f.sx):
                            ox = x + fx
                            if oy >= 0 and oy < V_sy and ox >= 0 and ox < V_sx:
                                for fd in range(f.depth):
                                    a += f.get(fx, fy, fd) * V.get(ox, oy, fd)
                    a += self.biases.get(0, 0, d)
                    A.set(ax, ay, d, a)
                    x += xy_stride
                y += xy_stride
        self.out_act = A
        return self.out_act

    def backward(self):
        V = self.in_act
        V.dw = np.zeros_like(V.w)
        V_sx = V.sx
        V_sy = V.sy
        xy_stride = self.stride
        for d in range(self.out_depth):
            f = self.filters[d]
            x = -self.pad
            y = -self.pad
            for ay in range(self.out_sy):
                y = -self.pad
                for ax in range(self.out_sx):
                    chain_grad = self.out_act.get_grad(ax, ay, d)
                    for fy in range(f.sy):
                        oy = y + fy
                        for fx in range(f.sx):
                            ox = x + fx
                            if oy >= 0 and oy < V_sy and ox >= 0 and ox < V_sx:
                                for fd in range(f.depth):
                                    ix1 = ((V_sx * oy) + ox) * V.depth + fd
                                    ix2 = ((f.sx * fy) + fx) * f.depth + fd
                                    f.add_grad(fx, fy, fd, V.w[ix1] * chain_grad)
                                    V.add_grad(ox, oy, fd, f.w[ix2] * chain_grad)
                    self.biases.add_grad(0, 0, d, chain_grad)
                    x += xy_stride
                y += xy_stride

    def getParamsAndGrads(self):
        response = []
        for i in range(self.out_depth):
            response.append({'params': self.filters[i].w, 'grads': self.filters[i].dw, 'l2_decay_mul': self.l2_decay_mul, 'l1_decay_mul': self.l1_decay_mul})
        response.append({'params': self.biases.w, 'grads': self.biases.dw, 'l1_decay_mul': 0.0, 'l2_decay_mul': 0.0})
        return response

def main():
    # Example usage of ConvLayer
    opt = {'filters': 10, 'sx': 3, 'in_depth': 3, 'in_sx': 32, 'in_sy': 32}
    conv_layer = ConvLayer(opt)
    # Forward pass
    input_volume = Vol(32, 32, 3, 0.0)
    output_volume = conv_layer.forward(input_volume)
    # Backward pass
    conv_layer.backward()

if __name__ == "__main__":
    main()
